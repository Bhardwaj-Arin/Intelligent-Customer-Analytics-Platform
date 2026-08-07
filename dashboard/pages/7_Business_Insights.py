"""
Business Insights Dashboard
------------------------------------------------------------

Pulls together sales, segmentation, and product data into one
executive-level view.

Project: Intelligent Customer Analytics Platform
"""

import plotly.express as px
import streamlit as st

from utils.cache import load_csv
from utils.config import PROCESSED_DATA_DIR
from utils.helper import format_currency

# ==========================================================
# LOAD DATA
# ==========================================================

sales_df = load_csv(PROCESSED_DATA_DIR / "final_cleaned_dataset.csv.gz")
segment_df = load_csv(PROCESSED_DATA_DIR / "customer_segments.csv")

# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("📈 Business Insights")

st.markdown(
    """
An executive-level summary of the business, combining transaction
data with the customer segments from Phase 5.
"""
)

st.divider()

# ==========================================================
# KEY METRICS
# ==========================================================

st.header("📌 Key Metrics")

completed = sales_df[~sales_df["IsCancelled"]]

total_revenue = completed["Revenue"].sum()
total_orders = completed["InvoiceNo"].nunique()
avg_order_value = total_revenue / total_orders
total_customers = sales_df["CustomerID"].nunique()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Revenue", format_currency(total_revenue))
k2.metric("Total Orders", f"{total_orders:,}")
k3.metric("Avg. Order Value", format_currency(avg_order_value))
k4.metric("Total Customers", f"{total_customers:,}")

st.divider()

# ==========================================================
# REVENUE BY SEGMENT
# ==========================================================

st.header("💼 Revenue by Customer Segment")

segment_revenue = (
    segment_df.groupby("CustomerSegment", as_index=False)["Monetary"]
    .sum()
    .sort_values("Monetary", ascending=False)
)
segment_revenue.columns = ["Segment", "Revenue"]

fig_segment_revenue = px.bar(
    segment_revenue,
    x="Revenue",
    y="Segment",
    orientation="h",
)
fig_segment_revenue.update_layout(
    height=340,
    yaxis=dict(autorange="reversed"),
    margin=dict(l=10, r=10, t=10, b=10),
)
st.plotly_chart(fig_segment_revenue, use_container_width=True)

st.divider()

# ==========================================================
# TOP PRODUCTS
# ==========================================================

st.header("🏆 Top 10 Products by Revenue")

st.caption(
    "Excludes non-product line items such as postage and manual "
    "adjustments (StockCode 'POST' and 'M')."
)

top_products = (
    completed[~completed["StockCode"].isin(["POST", "M"])]
    .groupby("Description", as_index=False)["Revenue"]
    .sum()
    .sort_values("Revenue", ascending=False)
    .head(10)
)

fig_products = px.bar(
    top_products.sort_values("Revenue"),
    x="Revenue",
    y="Description",
    orientation="h",
)
fig_products.update_layout(height=380, margin=dict(l=10, r=10, t=10, b=10))
st.plotly_chart(fig_products, use_container_width=True)

st.divider()

# ==========================================================
# MONTHLY ORDER VOLUME
# ==========================================================

st.header("📦 Monthly Order Volume")

monthly_orders = (
    completed.groupby(["Year", "Month"])["InvoiceNo"]
    .nunique()
    .reset_index(name="Orders")
)
monthly_orders["Period"] = (
    monthly_orders["Year"].astype(str)
    + "-"
    + monthly_orders["Month"].astype(str).str.zfill(2)
)
monthly_orders = monthly_orders.sort_values("Period")

fig_orders = px.line(monthly_orders, x="Period", y="Orders", markers=True)
fig_orders.update_layout(height=340, margin=dict(l=10, r=10, t=10, b=10))
st.plotly_chart(fig_orders, use_container_width=True)

st.divider()

# ==========================================================
# TAKEAWAYS
# ==========================================================

st.header("📝 Takeaways")

top_segment_row = segment_revenue.iloc[0]

st.info(
    f"**{top_segment_row['Segment']}** contributes the most revenue "
    f"of any segment, at {format_currency(top_segment_row['Revenue'])}."
)

st.info(
    f"Average order value across the business is "
    f"{format_currency(avg_order_value)}, across {total_orders:,} orders "
    f"from {total_customers:,} customers."
)

st.caption(
    "See the **Churn Prediction** and **CLV Prediction** pages for "
    "customer-level risk and value forecasts that feed into these "
    "numbers."
)
