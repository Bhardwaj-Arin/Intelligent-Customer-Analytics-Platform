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


# ============================================================
# Load CSV File
# ============================================================

@st.cache_data(show_spinner=False)
def load_csv(file_path):
    """
    Load a CSV file and cache the result.

    Parameters
    ----------
    file_path : str or Path

    Returns
    -------
    pandas.DataFrame
    """

    return pd.read_csv(file_path)


# ============================================================
# Load Pickle Model
# ============================================================

@st.cache_resource(show_spinner=False)
def load_model(model_path):
    """
    Load a trained machine learning model.

    Parameters
    ----------
    model_path : str or Path

    Returns
    -------
    Trained model object
    """

    return joblib.load(model_path)


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