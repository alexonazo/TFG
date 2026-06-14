"""Utilidades estables para exportaciones CSV."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

from .paths import ensure_directory


def clean_text_for_csv(value: object) -> str:
    """Normaliza saltos de linea y espacios para una celda CSV."""
    return " ".join(str(value).replace("\r", " ").replace("\n", " ").split()).strip()


def clean_dataframe_text_for_csv(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia columnas de texto de un DataFrame antes de exportarlo."""
    cleaned = df.copy()
    text_cols = cleaned.select_dtypes(include=["object", "string"]).columns
    for column in text_cols:
        cleaned[column] = cleaned[column].map(clean_text_for_csv)
    return cleaned


def safe_to_csv(df: pd.DataFrame, path: str | Path, index: bool = False, encoding: str = "utf-8-sig") -> Path:
    """Exporta un DataFrame creando antes la carpeta destino."""
    output_path = Path(path)
    ensure_directory(output_path.parent)
    df.to_csv(output_path, index=index, encoding=encoding)
    return output_path


def export_debug_snapshot(
    df: pd.DataFrame,
    output_path: str | Path,
    columns: Iterable[str],
    sort_col: str = "rank",
    max_rows: int = 100,
) -> pd.DataFrame:
    """Exporta un snapshot compacto de debug y devuelve lo exportado."""
    available_cols = [column for column in columns if column in df.columns]
    snapshot_source = df.sort_values(sort_col) if sort_col in df.columns else df
    snapshot = snapshot_source.head(max_rows)[available_cols].copy()
    snapshot = clean_dataframe_text_for_csv(snapshot)
    safe_to_csv(snapshot, output_path)
    return snapshot
