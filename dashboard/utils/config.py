'''
# Dashboard Configuration

## Objective

This module centralizes all dashboard configuration values.

Instead of hardcoding file paths, titles, colors, and page settings across multiple files, we store them in one place.

Benefits:

- Easier maintenance
- Cleaner code
- Single source of truth
- Better scalability
- Consistent dashboard settings
'''

"""
Dashboard Configuration
-----------------------

This module stores global configuration values used across
the Streamlit dashboard.

Author: Arin Bhardwaj
Project: Intelligent Customer Analytics Platform
"""

from pathlib import Path

# ============================================================
# Project Root Directory
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ============================================================
# Dashboard Information
# ============================================================

APP_TITLE = "Intelligent Customer Analytics Platform"

APP_ICON = "📊"

LAYOUT = "wide"

SIDEBAR_STATE = "expanded"

# ============================================================
# Data Paths
# ============================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

RECOMMENDATION_DATA_DIR = DATA_DIR / "recommendation"

# ============================================================
# Model Paths
# ============================================================

MODELS_DIR = PROJECT_ROOT / "models"

CLV_MODEL_PATH = MODELS_DIR / "clv_model.pkl"

CLV_SCALER_PATH = MODELS_DIR / "clv_scaler.pkl"

CHURN_MODEL_PATH = MODELS_DIR / "churn_model.pkl"

CHURN_SCALER_PATH = MODELS_DIR / "churn_scaler.pkl"

# ============================================================
# Assets
# ============================================================

ASSETS_DIR = PROJECT_ROOT / "assets"

LOGO_PATH = ASSETS_DIR / "logo.png"

BANNER_PATH = ASSETS_DIR / "banner.png"

WORKFLOW_PATH = ASSETS_DIR / "workflow.png"

ARCHITECTURE_PATH = ASSETS_DIR / "project_architecture.png"

# ============================================================
# Reports
# ============================================================

REPORTS_DIR = PROJECT_ROOT / "reports"

FIGURES_DIR = REPORTS_DIR / "figures"