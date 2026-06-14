"""Utilidades estables de normalizacion de scores."""

from __future__ import annotations

import numpy as np
import pandas as pd


def robust_normalize_score(
    series: pd.Series | list[float],
    lower_q: float = 0.01,
    upper_q: float = 0.99,
    default: float = 0.0,
) -> pd.Series:
    """Normaliza una serie a 0-1 usando cuantiles robustos."""
    values = (
        pd.to_numeric(pd.Series(series), errors="coerce")
        .replace([np.inf, -np.inf], np.nan)
        .fillna(default)
        .astype(float)
    )
    normalized = pd.Series(0.0, index=values.index, dtype=float)
    if values.empty:
        return normalized

    lower = float(values.quantile(lower_q))
    upper = float(values.quantile(upper_q))
    if not np.isfinite(lower) or not np.isfinite(upper) or upper <= lower:
        if values.max() > values.min():
            return ((values - values.min()) / (values.max() - values.min())).clip(0.0, 1.0).fillna(0.0)
        return normalized

    return ((values - lower) / (upper - lower)).clip(0.0, 1.0).fillna(0.0)


def rank_normalize_positive(series: pd.Series | list[float]) -> pd.Series:
    """Normaliza por ranking solo los valores positivos."""
    raw_scores = pd.to_numeric(pd.Series(series), errors="coerce").fillna(0.0)
    normalized = pd.Series(0.0, index=raw_scores.index, dtype=float)
    positive_mask = raw_scores > 0
    if positive_mask.any():
        normalized.loc[positive_mask] = raw_scores.loc[positive_mask].rank(pct=True)
    return normalized.clip(0.0, 1.0)


def has_real_variance(series: pd.Series | list[float], eps: float = 1e-9) -> bool:
    """Indica si una serie tiene mas de un valor util distinto."""
    values = pd.to_numeric(pd.Series(series), errors="coerce").dropna()
    return bool(values.nunique() > 1 and (values.max() - values.min()) > eps)
