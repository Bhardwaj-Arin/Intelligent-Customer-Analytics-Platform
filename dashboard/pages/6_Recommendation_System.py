"""
Recommendation System Dashboard
------------------------------------------------------------

Explores product recommendations from three approaches:

    - Popularity ranking (works for any customer, including new ones)
    - Customer-based collaborative filtering (similar customers)
    - Item-based collaborative filtering (similar products)

Project: Intelligent Customer Analytics Platform
"""

import plotly.express as px
import streamlit as st

from utils.cache import load_csv
from utils.config import RECOMMENDATION_DATA_DIR

# ==========================================================
# LOAD DATA
# ==========================================================

popularity_df = load_csv(
    RECOMMENDATION_DATA_DIR / "popularity_recommendations.csv"
)

collaborative_df = load_csv(
    RECOMMENDATION_DATA_DIR / "customer_collaborative_recommendations.csv"
)

# Add product descriptions to the collaborative recommendations by
# looking them up from the popularity table (both are keyed by
# StockCode).
collaborative_df = collaborative_df.merge(
    popularity_df[["StockCode", "Description"]].drop_duplicates("StockCode"),
    on="StockCode",
    how="left",
)

item_similarity_df = load_csv(
    RECOMMENDATION_DATA_DIR / "item_collaborative_recommendations.csv"
)

# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("🛍️ Recommendation System")

st.markdown(
    """
Three recommendation approaches were built for this project:

- **Popularity-based** — the best-selling products overall. Works
  for every customer, including ones with no purchase history.
- **Customer collaborative filtering** — finds customers with similar
  purchase patterns and recommends what *they* bought.
- **Item collaborative filtering** — finds products frequently
  bought together (using cosine similarity) and recommends similar
  items to what a customer already bought.

The last two only work for customers with enough purchase history
to find similar customers or products.
"""
)

st.divider()

# ==========================================================
# MOST POPULAR PRODUCTS
# ==========================================================

st.header("🔥 Most Popular Products")

top_n = st.slider("Number of products to show", 5, 30, 10)

top_products = popularity_df.sort_values(
    "PopularityRank"
).head(top_n)

fig_popular = px.bar(
    top_products.sort_values("PurchaseCount"),
    x="PurchaseCount",
    y="Description",
    orientation="h",
)
fig_popular.update_layout(height=420, margin=dict(l=10, r=10, t=10, b=10))
st.plotly_chart(fig_popular, use_container_width=True)

st.dataframe(
    top_products[
        ["StockCode", "Description", "PurchaseCount", "TotalRevenue"]
    ],
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# PERSONALIZED RECOMMENDATIONS
# ==========================================================

st.header("🎯 Customer Collaborative Filtering")

st.caption(
    f"Collaborative filtering recommendations are available for "
    f"{collaborative_df['CustomerID'].nunique():,} customers who have "
    f"enough purchase history to find similar customers."
)

available_customers = sorted(collaborative_df["CustomerID"].unique())

selected_customer = st.selectbox("Customer ID", available_customers)

customer_recs = collaborative_df[
    collaborative_df["CustomerID"] == selected_customer
].sort_values("NeighborCount", ascending=False)

rec_chart, rec_table = st.columns([1, 1])

with rec_chart:
    fig_customer_recs = px.bar(
        customer_recs.sort_values("NeighborCount"),
        x="NeighborCount",
        y="Description",
        orientation="h",
    )
    fig_customer_recs.update_layout(
        height=340,
        margin=dict(l=10, r=10, t=10, b=10),
    )
    st.plotly_chart(fig_customer_recs, use_container_width=True)

with rec_table:
    st.dataframe(
        customer_recs[["StockCode", "Description", "NeighborCount"]],
        use_container_width=True,
        hide_index=True,
    )

st.caption(
    "**NeighborCount** — how many similar customers also bought this "
    "product. Higher means more customers with similar taste "
    "purchased it."
)

st.divider()

# ==========================================================
# ITEM COLLABORATIVE FILTERING
# ==========================================================

st.header("🔗 Item Collaborative Filtering")

st.caption(
    f"Recommends products similar to what a customer has already "
    f"bought, based on cosine similarity between products. Available "
    f"for {item_similarity_df['CustomerID'].nunique():,} customers."
)

item_customers = sorted(item_similarity_df["CustomerID"].unique())

selected_item_customer = st.selectbox(
    "Customer ID",
    item_customers,
    key="item_similarity_customer",
)

item_recs = item_similarity_df[
    item_similarity_df["CustomerID"] == selected_item_customer
].sort_values("SimilarityScore", ascending=False)

item_chart, item_table = st.columns([1, 1])

with item_chart:
    fig_item_recs = px.bar(
        item_recs.sort_values("SimilarityScore"),
        x="SimilarityScore",
        y="Description",
        orientation="h",
    )
    fig_item_recs.update_layout(
        height=340,
        margin=dict(l=10, r=10, t=10, b=10),
    )
    st.plotly_chart(fig_item_recs, use_container_width=True)

with item_table:
    st.dataframe(
        item_recs[["StockCode", "Description", "SimilarityScore"]],
        use_container_width=True,
        hide_index=True,
    )