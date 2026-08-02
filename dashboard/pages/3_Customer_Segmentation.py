"""
Customer Segmentation Dashboard
-------------------------------------------------------------

This page explores the customer segments produced by the K-Means
clustering model trained on Recency, Frequency, and Monetary (RFM)
behaviour.

Every number, chart, and table on this page is computed directly
from the project's own segmentation outputs:

    - customer_segments.csv        -> segments_df
    - cluster_profile.csv          -> cluster_profile_df
    - business_segment_summary.csv -> business_summary_df

No external data, images, or text is used anywhere on this page.

Author: Arin Bhardwaj
Project: Intelligent Customer Analytics Platform
"""

import pandas as pd
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

st.title("👥 Customer Segmentation")

st.markdown(
    """
Customers are grouped into behavioural segments using **K-Means
clustering** on Recency, Frequency, and Monetary (RFM) features.

This page shows how many customers fall into each segment, what
separates one segment from another, and what the business should
do about it.
"""
)

st.divider()

# ==========================================================
# KPI OVERVIEW
# ==========================================================

st.header("📌 Segmentation at a Glance")

total_customers = segments_df["CustomerID"].nunique()

total_clusters = segments_df["Cluster"].nunique()

total_segments = segments_df["CustomerSegment"].nunique()

total_countries = segments_df["Country"].nunique()

avg_recency = segments_df["Recency"].mean()

avg_frequency = segments_df["Frequency"].mean()

avg_monetary = segments_df["Monetary"].mean()

avg_unique_products = segments_df["UniqueProducts"].mean()

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Customers",
        f"{total_customers:,}",
    )

with k2:

    st.metric(
        "Segments",
        total_segments,
    )

with k3:

    st.metric(
        "Clusters",
        total_clusters,
    )

with k4:

    st.metric(
        "Countries Covered",
        total_countries,
    )

k5, k6, k7, k8 = st.columns(4)

with k5:

    st.metric(
        "Avg Recency (days)",
        f"{avg_recency:.1f}",
    )

with k6:

    st.metric(
        "Avg Frequency",
        f"{avg_frequency:.1f}",
    )

with k7:

    st.metric(
        "Avg Monetary Value",
        format_currency(avg_monetary),
    )

with k8:

    st.metric(
        "Avg Unique Products",
        f"{avg_unique_products:.1f}",
    )

st.divider()

# ==========================================================
# SEGMENT DISTRIBUTION
# ==========================================================

st.header("📊 Segment Distribution")

segment_distribution = (
    segments_df["CustomerSegment"]
    .value_counts()
    .reset_index()
)

segment_distribution.columns = [
    "CustomerSegment",
    "Customers",
]

segment_distribution["Percentage"] = (
    segment_distribution["Customers"]
    / segment_distribution["Customers"].sum()
    * 100
).round(2)

dist_left, dist_right = st.columns([1, 1.2])

with dist_left:

    fig_segment_pie = px.pie(
        segment_distribution,
        names="CustomerSegment",
        values="Customers",
        hole=0.45,
        template="plotly_dark",
        title="Share of Customers by Segment",
    )

    fig_segment_pie.update_layout(
        height=400,
        margin=dict(l=10, r=10, t=40, b=10),
    )

    st.plotly_chart(
        fig_segment_pie,
        use_container_width=True,
    )

with dist_right:

    st.dataframe(
        segment_distribution,
        use_container_width=True,
        hide_index=True,
    )

st.divider()

# ==========================================================
# CLUSTER PROFILE
# ==========================================================

st.header("📌 Cluster Profile")

st.caption(
    "The raw RFM profile of each cluster produced by the K-Means model."
)

st.dataframe(
    cluster_profile_df[
        [
            "Cluster",
            "CustomerCount",
            "Recency",
            "Frequency",
            "Monetary",
            "TotalQuantity",
            "UniqueProducts",
            "AvgRevenue",
        ]
    ],
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# RFM COMPARISON ACROSS SEGMENTS
# ==========================================================

st.header("📈 RFM Comparison Across Segments")

st.caption(
    "Average Recency, Frequency, and Monetary value for each customer segment."
)

segment_rfm = (
    segments_df.groupby("CustomerSegment", as_index=False)
    .agg(
        Recency=("Recency", "mean"),
        Frequency=("Frequency", "mean"),
        Monetary=("Monetary", "mean"),
    )
    .round(2)
)

rfm_left, rfm_mid, rfm_right = st.columns(3)

with rfm_left:

    fig_recency = px.bar(
        segment_rfm.sort_values("Recency"),
        x="CustomerSegment",
        y="Recency",
        template="plotly_dark",
        title="Avg Recency (lower = more recent)",
    )

    fig_recency.update_layout(
        height=340,
        margin=dict(l=10, r=10, t=40, b=10),
    )

    st.plotly_chart(
        fig_recency,
        use_container_width=True,
    )

with rfm_mid:

    fig_frequency = px.bar(
        segment_rfm.sort_values("Frequency", ascending=False),
        x="CustomerSegment",
        y="Frequency",
        template="plotly_dark",
        title="Avg Frequency",
    )

    fig_frequency.update_layout(
        height=340,
        margin=dict(l=10, r=10, t=40, b=10),
    )

    st.plotly_chart(
        fig_frequency,
        use_container_width=True,
    )

with rfm_right:

    fig_monetary = px.bar(
        segment_rfm.sort_values("Monetary", ascending=False),
        x="CustomerSegment",
        y="Monetary",
        template="plotly_dark",
        title="Avg Monetary Value",
    )

    fig_monetary.update_layout(
        height=340,
        margin=dict(l=10, r=10, t=40, b=10),
    )

    st.plotly_chart(
        fig_monetary,
        use_container_width=True,
    )

st.divider()

# ==========================================================
# FREQUENCY vs MONETARY (SEGMENT BUBBLE MAP)
# ==========================================================

st.header("🫧 Customer Value Map — Frequency vs Monetary")

st.caption(
    "Each dot is a customer. Position shows Frequency and Monetary value; "
    "color shows the assigned segment; size shows unique products purchased."
)

sample_df = segments_df.sample(
    min(1500, len(segments_df)),
    random_state=42,
)

fig_bubble = px.scatter(
    sample_df,
    x="Frequency",
    y="Monetary",
    color="CustomerSegment",
    size="UniqueProducts",
    hover_data=["CustomerID", "Recency", "Country"],
    template="plotly_dark",
    render_mode="svg",
)

fig_bubble.update_layout(
    height=460,
    margin=dict(l=10, r=10, t=10, b=10),
)

st.plotly_chart(
    fig_bubble,
    use_container_width=True,
)

st.divider()

# ==========================================================
# TOP CUSTOMERS BY MONETARY VALUE
# ==========================================================

st.header("🏆 Top 15 Customers by Monetary Value")

top_monetary = (
    segments_df.sort_values("Monetary", ascending=False)
    .head(15)
)

fig_top_monetary = px.bar(
    top_monetary,
    x="Monetary",
    y=top_monetary["CustomerID"].astype(str),
    orientation="h",
    color="CustomerSegment",
    template="plotly_dark",
)

fig_top_monetary.update_layout(
    height=420,
    yaxis=dict(
        autorange="reversed",
        title="Customer ID",
    ),
    margin=dict(l=10, r=10, t=10, b=10),
)

st.plotly_chart(
    fig_top_monetary,
    use_container_width=True,
)

st.dataframe(
    top_monetary[
        [
            "CustomerID",
            "CustomerSegment",
            "Country",
            "Monetary",
            "Frequency",
            "Recency",
            "UniqueProducts",
        ]
    ],
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# TOP CUSTOMERS BY FREQUENCY & AVERAGE REVENUE
# ==========================================================

st.header("🔄 Most Frequent & Highest Average-Revenue Customers")

freq_left, revenue_right = st.columns(2)

with freq_left:

    st.subheader("Most Frequent Customers")

    top_frequency = (
        segments_df.sort_values("Frequency", ascending=False)
        .head(10)
    )

    st.dataframe(
        top_frequency[
            [
                "CustomerID",
                "CustomerSegment",
                "Frequency",
                "Monetary",
                "Recency",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )

with revenue_right:

    st.subheader("Highest Average Revenue")

    top_avg_revenue = (
        segments_df.sort_values("AvgRevenue", ascending=False)
        .head(10)
    )

    st.dataframe(
        top_avg_revenue[
            [
                "CustomerID",
                "CustomerSegment",
                "AvgRevenue",
                "Monetary",
                "Frequency",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )

st.divider()

# ==========================================================
# FULL CLUSTER COMPARISON TABLE
# ==========================================================

st.header("📋 Full Cluster Comparison")

st.caption(
    "Every metric captured for each cluster, side by side, including total "
    "quantity purchased and revenue range."
)

cluster_comparison_columns = [
    "Cluster",
    "CustomerCount",
    "Recency",
    "Frequency",
    "Monetary",
    "TotalQuantity",
    "UniqueProducts",
    "AvgRevenue",
    "RevenueRange",
]

available_comparison_columns = [
    column
    for column in cluster_comparison_columns
    if column in cluster_profile_df.columns
]

cluster_comparison = cluster_profile_df[available_comparison_columns]

st.dataframe(
    cluster_comparison,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# SEGMENT LEADERBOARD
# ==========================================================

st.header("🥇 Segment Leaderboard")

st.caption(
    "Segments ranked by average monetary value per customer."
)

leaderboard = (
    segments_df.groupby("CustomerSegment", as_index=False)
    .agg(
        Customers=("CustomerID", "count"),
        AvgRevenue=("AvgRevenue", "mean"),
        AvgMonetary=("Monetary", "mean"),
        AvgFrequency=("Frequency", "mean"),
        AvgRecency=("Recency", "mean"),
    )
    .round(2)
    .sort_values("AvgMonetary", ascending=False)
)

st.dataframe(
    leaderboard,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# SEGMENT SHARE BY COUNTRY
# ==========================================================

st.header("🌍 Segment Mix by Top Countries")

st.caption(
    "How the customer segment mix differs across the top 8 countries by customer count."
)

top_country_list = (
    segments_df["Country"]
    .value_counts()
    .head(8)
    .index
    .tolist()
)

country_segment_df = segments_df[
    segments_df["Country"].isin(top_country_list)
]

country_segment_summary = (
    country_segment_df.groupby(
        ["Country", "CustomerSegment"],
        as_index=False,
    )["CustomerID"]
    .count()
    .rename(columns={"CustomerID": "Customers"})
)

fig_country_segment = px.bar(
    country_segment_summary,
    x="Country",
    y="Customers",
    color="CustomerSegment",
    barmode="stack",
    template="plotly_dark",
)

fig_country_segment.update_layout(
    height=420,
    margin=dict(l=10, r=10, t=10, b=10),
)

st.plotly_chart(
    fig_country_segment,
    use_container_width=True,
)

st.divider()

# ==========================================================
# CUSTOMER EXPLORER
# ==========================================================

st.header("👤 Customer Explorer")

selected_customer = st.selectbox(
    "Select a Customer ID",
    sorted(segments_df["CustomerID"].unique()),
)

customer = segments_df[
    segments_df["CustomerID"] == selected_customer
].iloc[0]

ce1, ce2, ce3, ce4 = st.columns(4)

with ce1:

    st.metric(
        "Segment",
        customer["CustomerSegment"],
    )

with ce2:

    st.metric(
        "Recency (days)",
        f"{customer['Recency']:.0f}",
    )

with ce3:

    st.metric(
        "Frequency",
        f"{customer['Frequency']:.0f}",
    )

with ce4:

    st.metric(
        "Monetary",
        format_currency(customer["Monetary"]),
    )

st.caption(
    f"**Country:** {customer['Country']}  •  "
    f"**Unique Products Purchased:** {int(customer['UniqueProducts'])}  •  "
    f"**Average Revenue per Order:** {format_currency(customer['AvgRevenue'])}"
)

segment_avg = segment_rfm[
    segment_rfm["CustomerSegment"] == customer["CustomerSegment"]
].iloc[0]

comparison_df = pd.DataFrame(
    {
        "Metric": ["Recency", "Frequency", "Monetary"],
        "This Customer": [
            customer["Recency"],
            customer["Frequency"],
            customer["Monetary"],
        ],
        f"{customer['CustomerSegment']} Average": [
            segment_avg["Recency"],
            segment_avg["Frequency"],
            segment_avg["Monetary"],
        ],
    }
)

fig_customer_vs_segment = px.bar(
    comparison_df.melt(
        id_vars="Metric",
        var_name="Series",
        value_name="Value",
    ),
    x="Metric",
    y="Value",
    color="Series",
    barmode="group",
    template="plotly_dark",
    title="This Customer vs Segment Average",
)

fig_customer_vs_segment.update_layout(
    height=360,
    margin=dict(l=10, r=10, t=40, b=10),
)

st.plotly_chart(
    fig_customer_vs_segment,
    use_container_width=True,
)

st.divider()

# ==========================================================
# SEGMENT EXPLORER
# ==========================================================

st.header("🔍 Segment Explorer")

selected_segment = st.selectbox(
    "Select a Customer Segment",
    sorted(segments_df["CustomerSegment"].unique()),
    key="segment_explorer",
)

segment_df = segments_df[
    segments_df["CustomerSegment"] == selected_segment
]

se1, se2, se3, se4 = st.columns(4)

with se1:

    st.metric(
        "Customers",
        f"{segment_df['CustomerID'].nunique():,}",
    )

with se2:

    st.metric(
        "Avg Monetary",
        format_currency(segment_df["Monetary"].mean()),
    )

with se3:

    st.metric(
        "Avg Frequency",
        f"{segment_df['Frequency'].mean():.1f}",
    )

with se4:

    st.metric(
        "Avg Recency",
        f"{segment_df['Recency'].mean():.1f}",
    )

segment_top_countries = (
    segment_df["Country"]
    .value_counts()
    .head(5)
    .reset_index()
)

segment_top_countries.columns = [
    "Country",
    "Customers",
]

fig_segment_countries = px.bar(
    segment_top_countries,
    x="Customers",
    y="Country",
    orientation="h",
    template="plotly_dark",
    title=f"Top Countries in the {selected_segment} Segment",
)

fig_segment_countries.update_layout(
    height=320,
    yaxis=dict(autorange="reversed"),
    margin=dict(l=10, r=10, t=40, b=10),
)

st.plotly_chart(
    fig_segment_countries,
    use_container_width=True,
)

st.divider()

# ==========================================================
# MONETARY DISTRIBUTION BY SEGMENT
# ==========================================================

st.header("📦 Monetary Distribution by Segment")

st.caption(
    "How spread out customer spending is within each segment — wider boxes "
    "mean more variation between customers in that segment."
)

fig_box = px.box(
    segments_df,
    x="CustomerSegment",
    y="Monetary",
    color="CustomerSegment",
    template="plotly_dark",
)

fig_box.update_layout(
    height=420,
    showlegend=False,
    margin=dict(l=10, r=10, t=10, b=10),
)

st.plotly_chart(
    fig_box,
    use_container_width=True,
)

st.divider()

# ==========================================================
# REVENUE EFFICIENCY PER SEGMENT
# ==========================================================

st.header("⚙️ Revenue Efficiency per Segment")

st.caption(
    "Average revenue per order versus average unique products purchased, "
    "for each segment. Bubble size reflects the number of customers in that segment."
)

segment_efficiency = (
    segments_df.groupby("CustomerSegment", as_index=False)
    .agg(
        Customers=("CustomerID", "count"),
        AvgRevenue=("AvgRevenue", "mean"),
        AvgUniqueProducts=("UniqueProducts", "mean"),
        AvgMonetary=("Monetary", "mean"),
    )
    .round(2)
)

fig_efficiency = px.scatter(
    segment_efficiency,
    x="AvgUniqueProducts",
    y="AvgRevenue",
    size="Customers",
    color="CustomerSegment",
    text="CustomerSegment",
    template="plotly_dark",
    render_mode="svg",
)

fig_efficiency.update_traces(textposition="top center")

fig_efficiency.update_layout(
    height=420,
    margin=dict(l=10, r=10, t=10, b=10),
)

st.plotly_chart(
    fig_efficiency,
    use_container_width=True,
)

st.dataframe(
    segment_efficiency,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# BUSINESS RECOMMENDATIONS
# ==========================================================

st.header("💼 What Each Segment Means for the Business")

st.caption(
    "Business interpretation and recommended strategy generated for each segment."
)

for _, row in business_summary_df.iterrows():

    with st.container(border=True):

        st.subheader(row["Segment"])

        st.write(row["Business Interpretation"])

        st.caption(
            f"**Recommended strategy:** {row['Recommended Strategy']}"
        )

st.divider()

# ==========================================================
# INTERACTIVE FILTERS
# ==========================================================

st.header("🎛 Interactive Filters")

filter_col1, filter_col2 = st.columns(2)

with filter_col1:

    filter_segment = st.selectbox(
        "Customer Segment",
        ["All"] + sorted(segments_df["CustomerSegment"].unique().tolist()),
        key="filter_segment",
    )

with filter_col2:

    filter_country = st.selectbox(
        "Country",
        ["All"] + sorted(segments_df["Country"].unique().tolist()),
        key="filter_country",
    )

filtered_df = segments_df.copy()

if filter_segment != "All":

    filtered_df = filtered_df[
        filtered_df["CustomerSegment"] == filter_segment
    ]

if filter_country != "All":

    filtered_df = filtered_df[
        filtered_df["Country"] == filter_country
    ]

st.success(f"{len(filtered_df):,} customers selected.")

filter_kpi1, filter_kpi2, filter_kpi3, filter_kpi4 = st.columns(4)

with filter_kpi1:

    st.metric(
        "Customers",
        f"{filtered_df['CustomerID'].nunique():,}",
    )

with filter_kpi2:

    st.metric(
        "Avg Monetary",
        format_currency(filtered_df["Monetary"].mean()),
    )

with filter_kpi3:

    st.metric(
        "Avg Frequency",
        f"{filtered_df['Frequency'].mean():.2f}",
    )

with filter_kpi4:

    st.metric(
        "Avg Recency",
        f"{filtered_df['Recency'].mean():.2f}",
    )

st.dataframe(
    filtered_df.head(200),
    use_container_width=True,
    hide_index=True,
)

download_csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Filtered Customer Segments",
    data=download_csv,
    file_name="filtered_customer_segments.csv",
    mime="text/csv",
)

st.divider()

# ==========================================================
# KEY OBSERVATIONS (COMPUTED FROM THIS DATASET)
# ==========================================================

st.header("📌 Key Observations")

st.caption(
    "These insights are computed live from the segmentation data above - nothing here is hardcoded."
)

highest_value_segment = leaderboard.iloc[0]["CustomerSegment"]

largest_segment = (
    segments_df["CustomerSegment"]
    .value_counts()
    .idxmax()
)

most_recent_segment = segment_rfm.sort_values("Recency").iloc[0]["CustomerSegment"]

top_country_for_segments = (
    segments_df["Country"]
    .value_counts()
    .idxmax()
)

obs1, obs2 = st.columns(2)

with obs1:

    st.info(
        f"**Highest-value segment:** {highest_value_segment} customers "
        f"generate the most revenue per customer on average."
    )

    st.info(
        f"**Largest segment:** {largest_segment} has the most customers "
        f"of any segment in the dataset."
    )

with obs2:

    st.info(
        f"**Most recently active segment:** {most_recent_segment} customers "
        f"have purchased most recently on average."
    )

    st.info(
        f"**Largest customer base by country:** {top_country_for_segments} "
        f"contributes the most customers across all segments."
    )

st.divider()

# ==========================================================
# NAVIGATION
# ==========================================================

nav_left, nav_right = st.columns(2)

with nav_left:

    st.caption("⬅ Previous Page: Data Overview")

with nav_right:

    st.caption("➡ Next Page: CLV Prediction")