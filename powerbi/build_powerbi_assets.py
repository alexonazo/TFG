from __future__ import annotations

import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATASETS = ROOT / "powerbi" / "datasets"
PREVIEW_DIR = ROOT / "reports" / "figures" / "powerbi_preview"

CSV_PATHS = {
    "recomendaciones_finales": DATASETS / "recomendaciones_finales.csv",
    "perfil_usuario_trakt": DATASETS / "perfil_usuario_trakt.csv",
    "metricas_recomendador": DATASETS / "metricas_recomendador.csv",
    "distribucion_recomendaciones": DATASETS / "distribucion_recomendaciones.csv",
}

SENSITIVE_TERMS = ("token", "access_token", "refresh_token", "trakt_token")
BROKEN_TEXT_EXAMPLES = ("T?tulo", "valoraci?n", "Se?al")
BROKEN_TEXT_RE = re.compile(r"[^\W\d_]\?[^\W\d_]", re.UNICODE)


def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, encoding="utf-8-sig")


def validate_inputs(frames: dict[str, pd.DataFrame]) -> None:
    missing = [str(path) for path in CSV_PATHS.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("Faltan CSV obligatorios: " + ", ".join(missing))

    recs = frames["recomendaciones_finales"]
    if len(recs) != 20:
        raise ValueError(f"recomendaciones_finales debe tener 20 filas, tiene {len(recs)}.")

    required_rec_columns = {
        "rank",
        "title",
        "dominant_signal",
        "temporal_affinity_label",
        "final_recommendation_score",
        "false_positive_risk",
        "preference_margin_score",
    }
    missing_columns = sorted(required_rec_columns - set(recs.columns))
    if missing_columns:
        raise ValueError("Faltan columnas en recomendaciones_finales: " + ", ".join(missing_columns))

    rank = pd.to_numeric(recs["rank"], errors="coerce")
    expected_rank = pd.Series(range(1, len(recs) + 1), index=recs.index, dtype="int64")
    if not rank.notna().all() or not rank.astype("int64").equals(expected_rank):
        raise ValueError("La columna rank no esta ordenada de 1 a 20.")

    if recs["dominant_signal"].fillna("").astype(str).str.lower().eq("temporal").any():
        raise ValueError('dominant_signal contiene "temporal"; debe quedar como senal secundaria.')

    text_columns = []
    for name, frame in frames.items():
        object_columns = frame.select_dtypes(include=["object", "string"]).columns.tolist()
        text_columns.extend((name, column) for column in object_columns)
        for column in object_columns:
            values = frame[column].fillna("").astype(str)
            joined = "\n".join(values.tolist())
            lowered = joined.lower()
            found_sensitive = [term for term in SENSITIVE_TERMS if term in lowered]
            if found_sensitive:
                raise ValueError(f"Texto sensible detectado en {name}.{column}: {found_sensitive}")
            if any(example in joined for example in BROKEN_TEXT_EXAMPLES) or values.map(lambda value: bool(BROKEN_TEXT_RE.search(value))).any():
                raise ValueError(f"Posible texto roto por encoding en {name}.{column}.")

    if not text_columns:
        raise ValueError("No se detectaron columnas de texto para validar.")


def save_barh(series: pd.Series, title: str, xlabel: str, output: Path, color: str = "#4C78A8") -> None:
    data = series.dropna()
    if data.empty:
        raise ValueError(f"No hay datos para {title}.")
    data = data.sort_values(ascending=True)
    height = max(4.0, 0.45 * len(data) + 1.5)
    fig, ax = plt.subplots(figsize=(10, height))
    ax.barh(data.index.astype(str), data.values, color=color)
    ax.set_title(title, fontsize=14, weight="bold")
    ax.set_xlabel(xlabel)
    ax.grid(axis="x", alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(output, dpi=160)
    plt.close(fig)


def build_previews(frames: dict[str, pd.DataFrame]) -> list[Path]:
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    recs = frames["recomendaciones_finales"].copy()
    dist = frames["distribucion_recomendaciones"].copy()

    generated = []

    output = PREVIEW_DIR / "buckets.png"
    save_barh(recs["recommendation_bucket_label"].value_counts(), "Distribucion por tipo de recomendacion", "Peliculas", output)
    generated.append(output)

    output = PREVIEW_DIR / "senales_dominantes.png"
    save_barh(recs["dominant_signal_label"].value_counts(), "Senal principal de explicacion", "Peliculas", output, color="#59A14F")
    generated.append(output)

    output = PREVIEW_DIR / "generos.png"
    save_barh(recs["main_genre"].value_counts(), "Distribucion por genero principal", "Peliculas", output, color="#F28E2B")
    generated.append(output)

    decade_dist = dist.loc[dist["dimension"].eq("decade")].copy()
    decade_dist["count"] = pd.to_numeric(decade_dist["count"], errors="coerce")
    output = PREVIEW_DIR / "decadas.png"
    save_barh(decade_dist.set_index("category")["count"], "Distribucion por decada", "Peliculas", output, color="#E15759")
    generated.append(output)

    recs["false_positive_risk"] = pd.to_numeric(recs["false_positive_risk"], errors="coerce")
    recs["preference_margin_score"] = pd.to_numeric(recs["preference_margin_score"], errors="coerce")
    recs["final_recommendation_score"] = pd.to_numeric(recs["final_recommendation_score"], errors="coerce")
    fig, ax = plt.subplots(figsize=(9, 6))
    size = 120 + recs["final_recommendation_score"].fillna(0).clip(lower=0) * 260
    for bucket, subset in recs.groupby("recommendation_bucket_label"):
        ax.scatter(
            subset["false_positive_risk"],
            subset["preference_margin_score"],
            s=size.loc[subset.index],
            alpha=0.72,
            label=bucket,
        )
    ax.set_title("Margen positivo frente a riesgo de falso positivo", fontsize=14, weight="bold")
    ax.set_xlabel("false_positive_risk")
    ax.set_ylabel("preference_margin_score")
    ax.grid(alpha=0.2)
    ax.legend(loc="best", fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    output = PREVIEW_DIR / "score_vs_riesgo.png"
    fig.savefig(output, dpi=160)
    plt.close(fig)
    generated.append(output)

    top = recs.sort_values("rank", ascending=True).copy()
    output = PREVIEW_DIR / "top20_score.png"
    save_barh(top.set_index("title")["final_recommendation_score"], "Top 20 por score final", "final_recommendation_score", output, color="#B07AA1")
    generated.append(output)

    return generated


def main() -> None:
    frames = {name: read_csv(path) for name, path in CSV_PATHS.items()}
    validate_inputs(frames)
    generated = build_previews(frames)
    print("Validaciones Power BI OK.")
    print("PNGs generados:")
    for path in generated:
        print(f"- {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
