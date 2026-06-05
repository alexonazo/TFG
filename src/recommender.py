"""Funciones sencillas para un recomendador basado en generos."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def get_genre_columns(movies_df: pd.DataFrame) -> list[str]:
    """Devuelve las columnas que representan generos codificados."""
    base_columns = {
        "movieId",
        "title",
        "title_clean",
        "genres",
        "year",
        "rating_mean",
        "rating_count",
    }
    return [column for column in movies_df.columns if column not in base_columns]


def build_genre_feature_matrix(
    movies_df: pd.DataFrame,
    genre_columns: list[str],
) -> pd.DataFrame:
    """Construye una matriz de caracteristicas a partir de los generos."""
    return movies_df[genre_columns].fillna(0).astype(int)


def calculate_cosine_similarity(feature_matrix: pd.DataFrame | np.ndarray) -> np.ndarray:
    """Calcula la similitud coseno entre las filas de una matriz de caracteristicas."""
    return cosine_similarity(feature_matrix)


def find_movie_index(movies_df: pd.DataFrame, movie_title: str) -> int | None:
    """Busca una pelicula por titulo de forma flexible y devuelve su indice."""
    query = str(movie_title).strip().lower()
    if not query:
        print("Debes indicar un titulo de pelicula.")
        return None

    title_clean_series = _get_title_clean_series(movies_df)
    title_series = movies_df["title"].fillna("").str.lower()

    exact_matches = movies_df[(title_clean_series == query) | (title_series == query)]
    if not exact_matches.empty:
        candidates = _sort_movie_matches(exact_matches)
        if len(candidates) > 1:
            print("Se encontraron varias coincidencias exactas. Se usara la pelicula con mas valoraciones:")
            print(candidates[["title", "year", "rating_count"]].head(10).to_string(index=False))
        return int(candidates.index[0])

    partial_matches = movies_df[
        title_clean_series.str.contains(query, regex=False)
        | title_series.str.contains(query, regex=False)
    ]
    if partial_matches.empty:
        print(f"No se encontraron coincidencias para: {movie_title}")
        return None

    candidates = _sort_movie_matches(partial_matches)
    if len(candidates) > 1:
        print("Se encontraron varias coincidencias parciales. Se usara la pelicula con mas valoraciones:")
        print(candidates[["title", "year", "rating_count"]].head(10).to_string(index=False))
    return int(candidates.index[0])


def recommend_movies_by_genres(
    movies_df: pd.DataFrame,
    similarity_matrix: pd.DataFrame | np.ndarray,
    movie_title: str,
    n: int = 10,
    min_ratings: int = 20,
) -> pd.DataFrame:
    """Devuelve recomendaciones priorizando similitud y un minimo de valoraciones."""
    selected_index = find_movie_index(movies_df, movie_title)
    if selected_index is None:
        return _empty_recommendations()

    similarity_scores = _get_similarity_scores(similarity_matrix, selected_index)
    similar_indices = np.argsort(similarity_scores)[::-1]
    similar_indices = [idx for idx in similar_indices if idx != selected_index]

    output_columns = ["title", "year", "genres", "rating_mean", "rating_count"]
    working_columns = output_columns.copy()
    if "title_clean" in movies_df.columns:
        working_columns.insert(0, "title_clean")

    recommendations = movies_df.loc[similar_indices, working_columns].copy()
    if "title_clean" in recommendations.columns:
        recommendations["title"] = recommendations["title_clean"].fillna(recommendations["title"])

    recommendations["similarity_score"] = similarity_scores[similar_indices]
    recommendations = recommendations[
        ["title", "year", "genres", "rating_mean", "rating_count", "similarity_score"]
    ]
    recommendations = _prioritize_recommendations(
        recommendations,
        n=n,
        min_ratings=min_ratings,
    )

    print(f"Pelicula seleccionada: {movies_df.loc[selected_index, 'title']}")
    return recommendations


def _sort_movie_matches(matches_df: pd.DataFrame) -> pd.DataFrame:
    """Ordena coincidencias priorizando peliculas con mas valoraciones."""
    sort_columns: list[str] = []
    ascending: list[bool] = []

    if "rating_count" in matches_df.columns:
        sort_columns.append("rating_count")
        ascending.append(False)
    if "rating_mean" in matches_df.columns:
        sort_columns.append("rating_mean")
        ascending.append(False)

    if not sort_columns:
        return matches_df

    return matches_df.sort_values(sort_columns, ascending=ascending)


def _get_title_clean_series(movies_df: pd.DataFrame) -> pd.Series:
    """Devuelve una serie de titulos limpios si existe, o el titulo original."""
    if "title_clean" in movies_df.columns:
        return movies_df["title_clean"].fillna("").str.lower()
    return movies_df["title"].fillna("").str.lower()


def _get_similarity_scores(
    similarity_matrix: pd.DataFrame | np.ndarray,
    selected_index: int,
) -> np.ndarray:
    """Obtiene las similitudes para una pelicula desde una matriz o una tabla de rasgos."""
    if isinstance(similarity_matrix, pd.DataFrame):
        matrix_values = similarity_matrix.to_numpy()
    else:
        matrix_values = np.asarray(similarity_matrix)

    if matrix_values.ndim != 2:
        raise ValueError("La matriz de similitud o de caracteristicas debe tener dos dimensiones.")

    if matrix_values.shape[0] != matrix_values.shape[1]:
        return cosine_similarity(
            matrix_values[[selected_index]],
            matrix_values,
        ).flatten()

    return matrix_values[selected_index]


def _prioritize_recommendations(
    recommendations: pd.DataFrame,
    n: int,
    min_ratings: int,
) -> pd.DataFrame:
    """Ordena recomendaciones y prioriza peliculas con suficientes valoraciones."""
    sorted_recommendations = recommendations.sort_values(
        ["similarity_score", "rating_count", "rating_mean"],
        ascending=[False, False, False],
    )

    if min_ratings <= 0:
        return sorted_recommendations.head(n).reset_index(drop=True)

    high_confidence = sorted_recommendations[sorted_recommendations["rating_count"] >= min_ratings]
    fallback = sorted_recommendations[sorted_recommendations["rating_count"] < min_ratings]

    prioritized = pd.concat([high_confidence, fallback], ignore_index=True).head(n)

    if len(high_confidence) < n:
        print(
            "No hay suficientes peliculas similares con el minimo de valoraciones indicado. "
            "Se completan los resultados con peliculas menos valoradas."
        )

    return prioritized.reset_index(drop=True)


def _empty_recommendations() -> pd.DataFrame:
    """Crea un DataFrame vacio con el formato esperado para las recomendaciones."""
    return pd.DataFrame(
        columns=[
            "title",
            "year",
            "genres",
            "rating_mean",
            "rating_count",
            "similarity_score",
        ]
    )
