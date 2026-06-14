"""Validadores estables para diagnosticos finales."""

from __future__ import annotations

import pandas as pd

from .scoring_utils import has_real_variance


def require_columns(df: pd.DataFrame, columns: list[str], context: str = "DataFrame") -> None:
    """Lanza ``ValueError`` si faltan columnas obligatorias."""
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"{context} no tiene las columnas esperadas: {missing}")


def existing_columns(df: pd.DataFrame, columns: list[str]) -> list[str]:
    """Devuelve solo las columnas presentes en un DataFrame."""
    return [column for column in columns if column in df.columns]


def max_category_share(df: pd.DataFrame, column: str) -> float:
    """Calcula la cuota de la categoria mas frecuente."""
    if column not in df.columns or len(df) == 0:
        return 0.0
    counts = df[column].value_counts(dropna=False)
    return float(counts.max() / len(df)) if not counts.empty else 0.0


def build_debug_warnings(
    recommendations: pd.DataFrame,
    export_full_results: bool = False,
    frozen_order_ok: bool = True,
) -> list[str]:
    """Construye warnings finales sin modificar recomendaciones."""
    warnings_list: list[str] = []
    if not frozen_order_ok:
        warnings_list.append("El orden final cambio respecto a frozen_rank.")
    if export_full_results:
        warnings_list.append("EXPORT_FULL_RESULTS=True puede generar mas de un archivo; debe permanecer False.")

    if "final_recommendation_score" in recommendations.columns:
        score_range = recommendations["final_recommendation_score"].max() - recommendations["final_recommendation_score"].min()
        if score_range < 0.12:
            warnings_list.append("final_recommendation_score del top 20 tiene rango menor a 0.12.")

    if "recommendation_bucket" in recommendations.columns:
        if max_category_share(recommendations, "recommendation_bucket") > 0.70:
            warnings_list.append("recommendation_bucket concentra mas del 70% en una sola categoria.")
        if (recommendations["recommendation_bucket"] == "riesgo_controlado").mean() == 1.0:
            warnings_list.append("recommendation_bucket tiene 100% riesgo_controlado; revisar capa de salida.")
        if (recommendations["recommendation_bucket"] == "clasico_pendiente").mean() == 1.0:
            warnings_list.append("recommendation_bucket tiene 100% clasico_pendiente; revisar capa de salida.")

    if "dominant_signal" in recommendations.columns:
        if max_category_share(recommendations, "dominant_signal") > 0.75:
            warnings_list.append("dominant_signal concentra mas del 75% en una sola categoria.")
        if (recommendations["dominant_signal"] == "risk_penalized").mean() == 1.0:
            warnings_list.append("dominant_signal tiene 100% risk_penalized; revisar capa de salida.")
        if (recommendations["dominant_signal"] == "rerank_limited").mean() == 1.0:
            warnings_list.append("dominant_signal tiene 100% rerank_limited; revisar capa de salida.")
        if "rerank_jump_penalty" in recommendations.columns:
            rerank = pd.to_numeric(recommendations["rerank_jump_penalty"], errors="coerce").fillna(0.0)
            if not has_real_variance(rerank) and (recommendations["dominant_signal"] == "rerank_limited").any():
                warnings_list.append("rerank_limited aparece aunque rerank_jump_penalty no tiene varianza real.")

    if {"dominant_signal", "recommendation_bucket"}.issubset(recommendations.columns):
        invalid_risk = (recommendations["dominant_signal"] == "risk_penalized") & (
            recommendations["recommendation_bucket"] != "riesgo_controlado"
        )
        if invalid_risk.any():
            warnings_list.append("risk_penalized aparece en peliculas cuyo bucket no es riesgo_controlado.")

    if "explanation_display" in recommendations.columns:
        explanations = recommendations["explanation_display"].fillna("").astype(str).str.strip()
        if explanations.eq("").any():
            warnings_list.append("Hay explanation_display vacio.")
        shares = explanations.value_counts(normalize=True, dropna=False)
        if not shares.empty and float(shares.iloc[0]) > 0.60:
            warnings_list.append("explanation_display repite el mismo texto exacto en mas del 60% del top.")

    return warnings_list
