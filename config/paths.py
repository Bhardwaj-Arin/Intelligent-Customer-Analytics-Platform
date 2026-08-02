"""
Project Paths

Contains all folder paths used throughout the project.
"""

from pathlib import Path

# ------------------------------------------------------------------
# Project Root
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------------
# Data
# ------------------------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

INTERIM_DATA_DIR = DATA_DIR / "interim"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

# ------------------------------------------------------------------
# Reports
# ------------------------------------------------------------------

REPORTS_DIR = PROJECT_ROOT / "reports"

# ------------------------------------------------------------------
# Models
# ------------------------------------------------------------------

MODELS_DIR = PROJECT_ROOT / "models"

# ------------------------------------------------------------------
# Dashboard
# ------------------------------------------------------------------

DASHBOARD_DIR = PROJECT_ROOT / "dashboard"