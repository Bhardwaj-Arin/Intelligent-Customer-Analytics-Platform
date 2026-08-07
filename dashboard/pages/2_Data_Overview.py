"""
Data Overview Page
------------------------------------------------------------

Walks through the cleaned transaction dataset that every other
page in this dashboard is built on.

Project: Intelligent Customer Analytics Platform
"""

import plotly.express as px
import streamlit as st

from utils.data_loader import load_cleaned_data
from utils.helper import format_currency

# ==========================================================
# LOAD DATA
# ==========================================================

df = load_cleaned_data()

# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("🗂️ Data Overview")

st.markdown(
    """
The raw **Online Retail** dataset contained duplicate rows,
cancelled orders mixed in with completed ones, missing customer
IDs, and a handful of negative or zero prices. Phase 2 of this
project cleaned all of that up. This page shows what the cleaned
dataset looks like.
"""
)

st.divider()

# ==========================================================
# DATASET SUMMARY
# ==========================================================

st.header("📌 Dataset Summary")

k1, k2, k3, k4 = st.columns(4)

k1.metric("Rows", f"{len(df):,}")
k2.metric("Customers", f"{df['CustomerID'].nunique():,}")
k3.metric("Countries", f"{df['Country'].nunique():,}")
k4.metric("Cancelled Orders", f"{df['IsCancelled'].mean():.1%}")

st.caption(
    f"Date range: **{df['InvoiceDate'].min()}** to "
    f"**{df['InvoiceDate'].max()}**"
)

st.divider()

# ==========================================================
# SAMPLE DATA
# ==========================================================

st.header("👀 Sample Rows")

st.dataframe(
    df.head(20)[
        [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "UnitPrice",
            "Revenue",
            "CustomerID",
            "Country",
            "InvoiceDate",
            "IsCancelled",
        ]
    ],
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# TOP COUNTRIES BY REVENUE
# ==========================================================

st.header("🌍 Revenue by Country")

country_revenue = (
    df[~df["IsCancelled"]]
    .groupby("Country", as_index=False)["Revenue"]
    .sum()
    .sort_values("Revenue", ascending=False)
    .head(10)
)

fig_country = px.bar(
    country_revenue,
    x="Revenue",
    y="Country",
    orientation="h",
)
fig_country.update_layout(
    height=380,
    yaxis=dict(autorange="reversed"),
    margin=dict(l=10, r=10, t=10, b=10),
)
st.plotly_chart(fig_country, use_container_width=True)

st.caption(
    "The dataset is heavily UK-weighted — most transactions and "
    "revenue come from the United Kingdom, with Germany, Ireland "
    "and France as the next largest markets."
)

st.divider()

# ==========================================================
# SALES BY TIME OF DAY
# ==========================================================

st.header("🕒 When Do Customers Buy?")

time_of_day = (
    df[~df["IsCancelled"]]["TimeOfDay"]
    .value_counts()
    .reset_index()
)
time_of_day.columns = ["TimeOfDay", "Orders"]

fig_time = px.bar(time_of_day, x="TimeOfDay", y="Orders")
fig_time.update_layout(height=340, margin=dict(l=10, r=10, t=10, b=10))
st.plotly_chart(fig_time, use_container_width=True)

st.divider()

# ==========================================================
# CANCELLATIONS
# ==========================================================

st.header("↩️ Cancelled Orders")

st.caption(
    "Cancelled transactions (invoices starting with 'C') are kept "
    "in the dataset and flagged with `IsCancelled`, but excluded "
    "from every revenue figure shown across this dashboard."
)

c1, c2 = st.columns(2)
c1.metric("Cancelled Transactions", f"{df['IsCancelled'].sum():,}")
c2.metric(
    "Revenue Lost to Cancellations",
    format_currency(df.loc[df["IsCancelled"], "Revenue"].abs().sum()),
)
