"""Funciones sencillas de limpieza y transformacion de datos."""

from __future__ import annotations

import re
from typing import Any

import pandas as pd


def extract_year_from_title(title: Any) -> int | None:
    """Extrae el ano final de un titulo si tiene el formato ``(YYYY)``."""
    if pd.isna(title):
        return None

    match = re.search(r"\((\d{4})\)$", str(title))
    if match is None:
        return None

    return int(match.group(1))


def clean_title(title: Any) -> str | None:
    """Elimina el ano final del titulo y devuelve solo el nombre de la pelicula."""
    if pd.isna(title):
        return None

    cleaned = re.sub(r"\s*\(\d{4}\)$", "", str(title)).strip()
    return cleaned or None


def split_genres(genres: Any) -> list[str]:
    """Divide una cadena de generos separada por ``|`` en una lista simple."""
    if pd.isna(genres):
        return []

    genres_text = str(genres).strip()
    if not genres_text or genres_text == "(no genres listed)":
        return []

    return [genre for genre in genres_text.split("|") if genre]


def create_genre_one_hot(movies_df: pd.DataFrame) -> pd.DataFrame:
    """Crea una tabla con ``movieId`` y variables one-hot de generos."""
    genres_normalized = movies_df["genres"].apply(lambda value: "|".join(split_genres(value)))
    genre_dummies = genres_normalized.str.get_dummies(sep="|")
    return pd.concat([movies_df[["movieId"]], genre_dummies], axis=1)


def calculate_rating_summary(ratings_df: pd.DataFrame) -> pd.DataFrame:
    """Calcula la media y el numero de valoraciones por pelicula."""
    return (
        ratings_df.groupby("movieId", as_index=False)
        .agg(rating_mean=("rating", "mean"), rating_count=("rating", "count"))
    )


def build_movies_clean(movies_df: pd.DataFrame, ratings_df: pd.DataFrame) -> pd.DataFrame:
    """Construye una tabla final de peliculas limpia y enriquecida."""
    movies_clean = movies_df.copy()

    movies_clean["genres"] = movies_clean["genres"].fillna("")
    movies_clean.loc[movies_clean["genres"] == "(no genres listed)", "genres"] = ""
    movies_clean["year"] = movies_clean["title"].apply(extract_year_from_title)
    movies_clean["title_clean"] = movies_clean["title"].apply(clean_title)

    genre_encoded = create_genre_one_hot(movies_clean)
    rating_summary = calculate_rating_summary(ratings_df)

    movies_clean = movies_clean.merge(rating_summary, on="movieId", how="left")
    movies_clean = movies_clean.merge(genre_encoded, on="movieId", how="left")
    movies_clean["rating_count"] = movies_clean["rating_count"].fillna(0).astype(int)

    return movies_clean
