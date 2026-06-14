"""Utilidades estables para explicaciones finales."""

from __future__ import annotations

from typing import Any

import pandas as pd


def clean_anchor_names(value: Any, max_items: int = 2) -> str:
    """Limpia una lista/cadena de anclas y conserva pocas entradas."""
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass

    raw = str(value).replace(";", "|").replace(",", "|")
    anchors: list[str] = []
    for item in raw.split("|"):
        cleaned = " ".join(str(item).split()).strip(" -")
        if cleaned and cleaned.lower() not in {"nan", "none"} and cleaned not in anchors:
            anchors.append(cleaned)
    return " y ".join(anchors[:max_items])


def build_explanation_display(row: pd.Series | dict[str, Any]) -> str:
    """Construye una explicacion final breve desde bucket y senal dominante."""
    bucket = str(row.get("recommendation_bucket", "descubrimiento_compatible"))
    signal = str(row.get("dominant_signal", "margin"))
    branch = str(row.get("recommendation_branch", row.get("semantic_branch", "perfil principal"))).replace("_", " ")
    anchors = clean_anchor_names(row.get("anchor_movies_matched", ""))

    if bucket == "apuesta_segura":
        text = "Recomendacion segura: combina buen encaje con tu perfil, bajo riesgo de falso positivo y buena evidencia del modelo base."
    elif bucket == "muy_parecida_a_favoritas":
        text = (
            f"Recomendacion cercana a tus favoritas: comparte senales con {anchors} y mantiene buen margen frente al perfil negativo."
            if anchors
            else "Recomendacion cercana a tus favoritas: comparte senales de anclaje fuertes y mantiene buen margen frente al perfil negativo."
        )
    elif bucket == "clasico_pendiente":
        text = "Titulo consolidado compatible: entra por calidad, afinidad razonable con tu perfil y control de riesgo."
    elif bucket == "riesgo_controlado":
        text = "Recomendacion con riesgo controlado: tiene senales positivas, pero tambien algun factor de incertidumbre detectado por el modelo."
    else:
        text = f"Descubrimiento compatible: no es la opcion mas obvia, pero encaja con la rama {branch} y mantiene buen margen positivo frente al perfil negativo."

    details = []
    if bucket != "descubrimiento_compatible" and branch:
        details.append(f"Rama: {branch}.")
    if signal == "margin":
        details.append("Senal principal: margen positivo frente al perfil negativo.")
    elif signal == "anchor" and anchors:
        details.append(f"Senal principal: anclas coherentes ({anchors}).")
    elif signal == "quality":
        details.append("Senal principal: calidad y evidencia base consolidadas.")
    elif signal == "temporal":
        details.append("Senal principal: encaje temporal personalizado.")
    elif signal == "semantic":
        details.append("Senal principal: similitud semantica con tus preferencias.")
    elif signal == "collaborative":
        details.append("Senal principal: afinidad colaborativa item-item.")
    elif signal == "popularity":
        details.append("Senal principal: popularidad compatible con el perfil.")
    elif signal == "rerank_limited":
        details.append("Senal principal: salto de reranking limitado por prudencia.")
    elif signal == "risk_penalized":
        details.append("Senal principal: riesgo relativo revisado de forma explicita.")
    return " ".join([text] + details).strip()
