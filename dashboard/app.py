"""
Main Dashboard Application
--------------------------

Entry point for the Intelligent Customer Analytics Platform.

Author: Arin Bhardwaj
"""

from pathlib import Path

import streamlit as st

from utils.config import (
    APP_ICON,
    APP_TITLE,
    LAYOUT,
    SIDEBAR_STATE,
)

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE,
)

# ==========================================================
# Load Custom CSS
# ==========================================================

css_file = Path(__file__).parent / "styles" / "style.css"

if css_file.exists():
    with open(css_file, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )

# ==========================================================
# Dashboard Header
# ==========================================================

st.title("📊 Intelligent Customer Analytics Platform")

st.markdown("---")

st.markdown(
    """
Welcome to the **Intelligent Customer Analytics Platform**.

Use the **sidebar** to navigate through the different dashboard pages.

This dashboard integrates:

- Customer Analytics
- Customer Segmentation
- Customer Lifetime Value Prediction
- Customer Churn Prediction
- Hybrid Recommendation System
- Business Insights

All models and analytics presented here were developed during Phases 1–8 of the project.
"""
)

st.info(
    "👈 Select a page from the sidebar to begin exploring the dashboard."
)