'''
# Dashboard Data Loader

## Objective

The objective of this module is to centralize the loading of all datasets used throughout the Streamlit dashboard.

Instead of manually loading CSV files on every dashboard page, we create reusable functions that load the required datasets.

Benefits:

- Eliminates duplicate code
- Improves maintainability
- Reduces chances of loading incorrect files
- Works seamlessly with the caching system
- Provides a single source of truth for all dashboard datasets
'''


"""
Dashboard Data Loader
---------------------

This module contains functions for loading all datasets
used throughout the Streamlit dashboard.

Author: Arin Bhardwaj
Project: Intelligent Customer Analytics Platform
"""

from utils.cache import load_csv
from utils.config import (
    PROCESSED_DATA_DIR,
    RECOMMENDATION_DATA_DIR,
)


# ============================================================
# Phase 2
# ============================================================

def load_cleaned_data():
    """
    Load the final cleaned dataset.
    """
    return load_csv(
        PROCESSED_DATA_DIR / "final_cleaned_dataset.csv"
    )


# ============================================================
# Phase 4
# ============================================================

def load_customer_features():
    """
    Load customer feature dataset.
    """
    return load_csv(
        PROCESSED_DATA_DIR / "customer_features.csv"
    )


# ============================================================
# Phase 5
# ============================================================

def load_customer_segments():
    """
    Load customer segmentation dataset.
    """
    return load_csv(
        PROCESSED_DATA_DIR / "customer_segments.csv"
    )


def load_cluster_profile():
    """
    Load cluster profile.
    """
    return load_csv(
        PROCESSED_DATA_DIR / "cluster_profile.csv"
    )


def load_business_segment_summary():
    """
    Load business summary for customer segments.
    """
    return load_csv(
        PROCESSED_DATA_DIR / "business_segment_summary.csv"
    )


# ============================================================
# Phase 6
# ============================================================

def load_clv_dataset():
    """
    Load CLV prediction dataset.
    """
    return load_csv(
        PROCESSED_DATA_DIR / "customer_clv_dataset.csv"
    )


def load_clv_predictions():
    """
    Load CLV prediction results.
    """
    return load_csv(
        PROCESSED_DATA_DIR / "customer_clv_predictions.csv"
    )


# ============================================================
# Phase 7
# ============================================================

def load_churn_dataset():
    """
    Load churn prediction dataset.
    """
    return load_csv(
        PROCESSED_DATA_DIR / "customer_churn_dataset.csv"
    )


def load_churn_predictions():
    """
    Load churn prediction results.
    """
    return load_csv(
        PROCESSED_DATA_DIR / "customer_churn_predictions.csv"
    )


# ============================================================
# Phase 8
# ============================================================

def load_popularity_recommendations():
    """
    Load popularity-based recommendations.
    """
    return load_csv(
        RECOMMENDATION_DATA_DIR /
        "popularity_recommendations.csv"
    )


def load_customer_collaborative():
    """
    Load customer collaborative recommendations.
    """
    return load_csv(
        RECOMMENDATION_DATA_DIR /
        "customer_collaborative_recommendations.csv"
    )


def load_item_collaborative():
    """
    Load item collaborative recommendations.
    """
    return load_csv(
        RECOMMENDATION_DATA_DIR /
        "item_collaborative_recommendations.csv"
    )