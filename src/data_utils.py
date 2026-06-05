"""Utilidades simples para cargar y explorar datasets."""

from pathlib import Path

import pandas as pd


def _to_path(path):
    """Convierte una ruta en un objeto ``Path``."""
    return Path(path)


def load_movies(path):
    """Carga el archivo de peliculas en un DataFrame."""
    return pd.read_csv(_to_path(path))


def load_ratings(path):
    """Carga el archivo de valoraciones en un DataFrame."""
    return pd.read_csv(_to_path(path))


def load_tags(path):
    """Carga el archivo de etiquetas en un DataFrame."""
    return pd.read_csv(_to_path(path))


def load_links(path):
    """Carga el archivo de enlaces en un DataFrame."""
    return pd.read_csv(_to_path(path))


def show_basic_info(df, name):
    """Muestra informacion basica de un DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame que se quiere revisar.
    name : str
        Nombre descriptivo del dataset.
    """
    print(f"{name}")
    print(f"Shape: {df.shape}")
    print("Columns:", list(df.columns))
    print(df.head())
