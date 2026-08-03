'''
# Dashboard Cache Module

## Objective

The objective of this module is to improve the dashboard's performance by caching expensive operations.

Without caching, every user interaction (button click, slider movement, page refresh) would reload datasets and machine learning models from disk.

Using Streamlit's caching mechanism allows the application to load data and models once and reuse them, resulting in a much faster and more responsive dashboard.

Benefits:

- Faster dashboard performance
- Reduced disk I/O
- Lower memory overhead
- Better user experience
- Cleaner code
'''

"""
Dashboard Cache Module
----------------------

This module provides reusable caching decorators for
loading datasets and machine learning models efficiently.

Author: Arin Bhardwaj
Project: Intelligent Customer Analytics Platform
"""

import joblib
import pandas as pd
import streamlit as st

from pathlib import Path


# ============================================================
# Load CSV File
# ============================================================

def _file_fingerprint(file_path):
    """
    Build a small fingerprint of a file's current state (its
    last-modified time and size).

    st.cache_data keys its cache on a function's arguments, not
    on what a file on disk actually contains. If a CSV is fixed
    or replaced without the app process itself restarting (for
    example, after a "soft" code-only redeploy on Streamlit
    Cloud), the old cached DataFrame would otherwise keep being
    served forever. Passing this fingerprint alongside the file
    path means the cache key changes whenever the file changes,
    so a stale cache can never outlive the file it came from.
    """

    path = Path(file_path)

    if not path.exists():
        return "missing"

    file_stats = path.stat()

    return f"{file_stats.st_mtime_ns}-{file_stats.st_size}"


@st.cache_data(show_spinner=False)
def _load_csv_cached(file_path, _fingerprint):
    return pd.read_csv(file_path)


def load_csv(file_path):
    """
    Load a CSV file and cache the result.

    The cache automatically invalidates if the file's contents
    change on disk, even if the app process wasn't restarted.

    Parameters
    ----------
    file_path : str or Path

    Returns
    -------
    pandas.DataFrame
    """

    return _load_csv_cached(file_path, _file_fingerprint(file_path))


# ============================================================
# Load Pickle Model
# ============================================================

def _load_model_cached_key(model_path):
    return _file_fingerprint(model_path)


@st.cache_resource(show_spinner=False)
def _load_model_cached(model_path, _fingerprint):
    return joblib.load(model_path)


def load_model(model_path):
    """
    Load a trained machine learning model.

    The cache automatically invalidates if the model file's
    contents change on disk, even if the app process wasn't
    restarted.

    Parameters
    ----------
    model_path : str or Path

    Returns
    -------
    Trained model object
    """

    return _load_model_cached(model_path, _file_fingerprint(model_path))


# ============================================================
# Clear All Cache
# ============================================================

def clear_dashboard_cache():
    """
    Clear Streamlit cache.

    Useful during development.
    """

    st.cache_data.clear()
    st.cache_resource.clear()