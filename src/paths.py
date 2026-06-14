"""Utilidades estables para rutas del proyecto."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


def project_root_from(start: str | Path | None = None) -> Path:
    """Devuelve la raiz del proyecto buscando una carpeta ``data``."""
    current = Path(start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "data").is_dir():
            return candidate
    return current


def ensure_directory(path: str | Path) -> Path:
    """Crea una carpeta si no existe y devuelve su ``Path``."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def ensure_directories(paths: Iterable[str | Path]) -> list[Path]:
    """Crea varias carpetas y devuelve sus rutas normalizadas."""
    return [ensure_directory(path) for path in paths]


def reports_debug_path(root: str | Path) -> Path:
    """Devuelve la carpeta de debug dentro de ``reports``."""
    return Path(root) / "reports" / "debug"


def reports_resultados_path(root: str | Path) -> Path:
    """Devuelve la carpeta de resultados dentro de ``reports``."""
    return Path(root) / "reports" / "resultados"
