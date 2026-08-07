"""
Customer Segmentation Dashboard
------------------------------------------------------------

Explores the customer segments produced by K-Means clustering
on Recency, Frequency, and Monetary (RFM) behaviour.

Project: Intelligent Customer Analytics Platform
"""

import plotly.express as px
import streamlit as st

from utils.data_loader import (
    load_business_segment_summary,
    load_cluster_profile,
    load_customer_segments,
)
from utils.helper import format_currency

# ==========================================================
# LOAD DATA
# ==========================================================

segments_df = load_customer_segments()
cluster_profile_df = load_cluster_profile()
business_summary_df = load_business_segment_summary()

# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("🧩 Customer Segmentation")

st.markdown(
    """
Customers were grouped using **K-Means clustering** on their RFM
behaviour — **R**ecency (days since last purchase), **F**requency
(number of orders), and **M**onetary value (total spend). This
splits the customer base into groups with similar purchasing
patterns, so each group can be treated differently.
"""
)

st.divider()

# ==========================================================
# SEGMENT OVERVIEW
# ==========================================================

st.header("📌 Segment Overview")

k1, k2 = st.columns(2)
k1.metric("Total Customers", f"{len(segments_df):,}")
k2.metric("Segments", f"{segments_df['CustomerSegment'].nunique():,}")

segment_counts = (
    segments_df["CustomerSegment"]
    .value_counts()
    .reset_index()
)
segment_counts.columns = ["Segment", "Customers"]

fig_segments = px.bar(
    segment_counts.sort_values("Customers"),
    x="Customers",
    y="Segment",
    orientation="h",
)
fig_segments.update_layout(height=340, margin=dict(l=10, r=10, t=10, b=10))
st.plotly_chart(fig_segments, use_container_width=True)

st.divider()

# ==========================================================
# WHAT EACH SEGMENT MEANS
# ==========================================================

st.header("🏷️ What Each Segment Means")

st.dataframe(
    business_summary_df,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# CLUSTER PROFILE (THE RAW RFM NUMBERS)
# ==========================================================

st.header("📊 Average RFM by Cluster")

st.caption(
    "The actual behaviour behind each cluster — useful for checking "
    "whether a segment's name matches its numbers."
)

st.dataframe(
    cluster_profile_df[
        ["Cluster", "Recency", "Frequency", "Monetary", "CustomerCount"]
    ].round(2),
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# CUSTOMER EXPLORER
# ==========================================================

st.header("👤 Explore by Segment")

selected_segment = st.selectbox(
    "Segment",
    sorted(segments_df["CustomerSegment"].unique()),
)

segment_customers = segments_df[
    segments_df["CustomerSegment"] == selected_segment
]

e1, e2, e3 = st.columns(3)
e1.metric("Customers", f"{len(segment_customers):,}")
e2.metric("Avg. Recency", f"{segment_customers['Recency'].mean():.0f} days")
e3.metric(
    "Avg. Monetary",
    format_currency(segment_customers["Monetary"].mean()),
)

st.dataframe(
    segment_customers[
        ["CustomerID", "Country", "Recency", "Frequency", "Monetary"]
    ].head(50),
    use_container_width=True,
    hide_index=True,
)
