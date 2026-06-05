"""Funciones sencillas para evaluar resultados del recomendador."""

from __future__ import annotations

from collections.abc import Iterable

import pandas as pd


def calculate_recommendation_summary(recommendations_df: pd.DataFrame) -> dict[str, float | int]:
    """Calcula un resumen simple de un conjunto de recomendaciones."""
    if recommendations_df.empty:
        return {
            "num_recommendations": 0,
            "similarity_mean": 0.0,
            "rating_mean_mean": 0.0,
            "rating_count_mean": 0.0,
        }

    return {
        "num_recommendations": int(len(recommendations_df)),
        "similarity_mean": float(recommendations_df["similarity_score"].mean()),
        "rating_mean_mean": float(recommendations_df["rating_mean"].mean()),
        "rating_count_mean": float(recommendations_df["rating_count"].mean()),
    }


def compare_genres(
    original_genres: str | None,
    recommended_genres: str | None,
) -> dict[str, object]:
    """Compara los generos de dos peliculas y devuelve su solapamiento."""
    original_set = _split_genres(original_genres)
    recommended_set = _split_genres(recommended_genres)
    shared_genres = sorted(original_set.intersection(recommended_set))

    return {
        "shared_genres": shared_genres,
        "shared_genres_count": len(shared_genres),
        "has_overlap": len(shared_genres) > 0,
    }


def build_evaluation_summary(results: list[dict[str, object]]) -> pd.DataFrame:
    """Convierte una lista de resultados de evaluacion en un DataFrame."""
    if not results:
        return pd.DataFrame(
            columns=[
                "input_movie",
                "num_recommendations",
                "similarity_mean",
                "rating_mean_mean",
                "rating_count_mean",
                "comment",
            ]
        )

    return pd.DataFrame(results)


def _split_genres(genres: str | None) -> set[str]:
    """Separa una cadena de generos en un conjunto sencillo."""
    if genres is None or pd.isna(genres):
        return set()

    if not isinstance(genres, str):
        if isinstance(genres, Iterable):
            return {str(value).strip() for value in genres if str(value).strip()}
        return set()

    return {genre.strip() for genre in genres.split("|") if genre.strip()}
