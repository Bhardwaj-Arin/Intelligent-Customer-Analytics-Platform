from pathlib import Path
import pandas as pd
import json
import joblib

ROOT_DIR = Path(__file__).resolve().parents[2]

ARTIFACT_DIR = ROOT_DIR / "artifacts"

SEGMENTATION_DIR = ARTIFACT_DIR / "segmentation"
CLV_DIR = ARTIFACT_DIR / "clv"
CHURN_DIR = ARTIFACT_DIR / "churn"
RECOMMENDATION_DIR = ARTIFACT_DIR / "recommendation"


# ==========================================================
# CUSTOMER SEGMENTATION
# ==========================================================

def load_customer_segments():
    return pd.read_csv(
        SEGMENTATION_DIR / "customer_segments.csv"
    )


def load_segment_summary():
    return pd.read_csv(
        SEGMENTATION_DIR / "segment_summary.csv"
    )


def load_cluster_centers():
    return pd.read_csv(
        SEGMENTATION_DIR / "cluster_centers.csv"
    )


def load_kmeans_metrics():
    return pd.read_csv(
        SEGMENTATION_DIR / "kmeans_metrics.csv"
    )


def load_silhouette_score():

    with open(
        SEGMENTATION_DIR / "silhouette_score.json",
        "r"
    ) as f:

        return json.load(f)


# ==========================================================
# CLV
# ==========================================================

def load_clv_predictions():
    return pd.read_csv(
        CLV_DIR / "clv_predictions.csv"
    )


def load_regression_metrics():
    return pd.read_csv(
        CLV_DIR / "regression_metrics.csv"
    )


def load_clv_feature_importance():
    return pd.read_csv(
        CLV_DIR / "feature_importance.csv"
    )


def load_residuals():
    return pd.read_csv(
        CLV_DIR / "residuals.csv"
    )


def load_actual_vs_predicted():
    return pd.read_csv(
        CLV_DIR / "actual_vs_predicted.csv"
    )


# ==========================================================
# CHURN
# ==========================================================

def load_churn_predictions():
    return pd.read_csv(
        CHURN_DIR / "churn_predictions.csv"
    )


def load_classification_metrics():
    return pd.read_csv(
        CHURN_DIR / "classification_metrics.csv"
    )


def load_confusion_matrix():
    return pd.read_csv(
        CHURN_DIR / "confusion_matrix.csv",
        index_col=0
    )


def load_churn_feature_importance():
    return pd.read_csv(
        CHURN_DIR / "feature_importance.csv"
    )


def load_roc_curve():
    return pd.read_csv(
        CHURN_DIR / "roc_curve.csv"
    )


# ==========================================================
# RECOMMENDATION
# ==========================================================

def load_association_rules():
    return pd.read_csv(
        RECOMMENDATION_DIR / "association_rules.csv"
    )


def load_recommendations():
    return pd.read_csv(
        RECOMMENDATION_DIR / "recommendations.csv"
    )


def load_recommendation_metrics():
    return pd.read_csv(
        RECOMMENDATION_DIR / "evaluation_metrics.csv"
    )


def load_item_similarity():
    return joblib.load(
        RECOMMENDATION_DIR / "item_similarity.pkl"
    )