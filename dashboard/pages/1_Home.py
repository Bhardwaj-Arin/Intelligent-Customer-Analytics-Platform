"""
Home Page
------------------------------------------------------------

Landing page: a quick snapshot of the dataset and what each
page in this dashboard covers.

Project: Intelligent Customer Analytics Platform
"""

import plotly.express as px
import streamlit as st

from utils.data_loader import load_cleaned_data
from utils.helper import format_currency

st.set_page_config(
    page_title="Intelligent Customer Analytics Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# LOAD DATA
# ==========================================================

df = load_cleaned_data()

# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("📊 Intelligent Customer Analytics Platform")

st.markdown(
    """
This dashboard turns raw e-commerce transactions into a set of
customer-level analytics: who the customers are, what they're
worth, who's likely to leave, and what to recommend them next.

It's built on the **Online Retail** dataset — real transaction
records from a UK-based online gift retailer, covering
December 2009 to December 2011.
"""
)

st.divider()

# ==========================================================
# DATASET SNAPSHOT
# ==========================================================

st.header("📌 Dataset Snapshot")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Transactions", f"{len(df):,}")
k2.metric("Customers", f"{df['CustomerID'].nunique():,}")
k3.metric("Countries", f"{df['Country'].nunique():,}")
k4.metric(
    "Total Revenue",
    format_currency(df.loc[~df["IsCancelled"], "Revenue"].sum()),
)

st.divider()

# ==========================================================
# REVENUE OVER TIME
# ==========================================================

st.header("📈 Revenue Over Time")

monthly_revenue = (
    df[~df["IsCancelled"]]
    .groupby(["Year", "Month"], as_index=False)["Revenue"]
    .sum()
)

monthly_revenue["Period"] = (
    monthly_revenue["Year"].astype(str)
    + "-"
    + monthly_revenue["Month"].astype(str).str.zfill(2)
)

monthly_revenue = monthly_revenue.sort_values("Period")

fig_revenue = px.line(
    monthly_revenue,
    x="Period",
    y="Revenue",
    markers=True,
)
fig_revenue.update_layout(height=380, margin=dict(l=10, r=10, t=10, b=10))
st.plotly_chart(fig_revenue, use_container_width=True)

st.divider()

# ==========================================================
# WHAT'S IN THIS DASHBOARD
# ==========================================================

st.header("🧭 What's in This Dashboard")

st.markdown(
    """
- **Data Overview** — how the raw transaction data was cleaned and what it looks like
- **Customer Segmentation** — grouping customers by purchase behaviour (RFM + K-Means)
- **CLV Prediction** — predicting each customer's future lifetime value
- **Churn Prediction** — predicting which customers are likely to stop buying
- **Recommendation System** — product recommendations based on purchase history
- **Business Insights** — pulling the analysis together into strategic takeaways
"""
)

st.info("👈 Use the sidebar to move between pages.")
