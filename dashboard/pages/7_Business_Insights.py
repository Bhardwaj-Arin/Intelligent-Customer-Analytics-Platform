"""
Business Insights Dashboard
-------------------------------------------------------------

This page brings together sales, customer, product and segment
data into one executive-level view, with strategic recommendations
drawn directly from the numbers.

Every number, chart, and table on this page is computed directly
from the project's own processed data:

    - final_cleaned_dataset.csv -> sales_df
    - customer_features.csv    -> customer_df
    - customer_segments.csv    -> segment_df

No external data, images, or text is used anywhere on this page.

Author: Arin Bhardwaj
Project: Intelligent Customer Analytics Platform
"""

import pandas as pd
import plotly.express as px
import streamlit as st

from utils.cache import load_csv
from utils.config import PROCESSED_DATA_DIR
from utils.helper import format_currency

# ==========================================================
# LOAD DATA (MEMORY-OPTIMIZED)
# ==========================================================
#
# final_cleaned_dataset.csv has ~800,000 rows. Left to guess
# dtypes on its own, pandas builds several text columns as the
# generic "object" dtype while reading the file, which is far
# heavier in memory than a proper category/numeric type and can
# raise a numpy ArrayMemoryError on machines with limited RAM.
# Passing dtypes directly into read_csv avoids ever building
# those expensive object arrays in the first place.


@st.cache_data(show_spinner=False)
def load_sales_data():

    dtype_map = {
        "Quantity": "int32",
        "Revenue": "float32",
        "CustomerID": "int32",
        "Country": "category",
        "Year": "int16",
        "Month": "int8",
        "MonthName": "category",
        "DayName": "category",
        "TimeOfDay": "category",
    }

    file_path = PROCESSED_DATA_DIR / "final_cleaned_dataset.csv"

    header_columns = pd.read_csv(file_path, nrows=0).columns.tolist()

    usable_dtypes = {
        column: dtype
        for column, dtype in dtype_map.items()
        if column in header_columns
    }

    return pd.read_csv(file_path, dtype=usable_dtypes)


@st.cache_data(show_spinner=False)
def load_customer_features_optimized():

    dtype_map = {
        "CustomerID": "int32",
        "Country": "category",
        "Frequency": "int32",
        "Monetary": "float32",
        "AvgRevenue": "float32",
        "UniqueProducts": "int32",
    }

    file_path = PROCESSED_DATA_DIR / "customer_features.csv"

    header_columns = pd.read_csv(file_path, nrows=0).columns.tolist()

    usable_dtypes = {
        column: dtype
        for column, dtype in dtype_map.items()
        if column in header_columns
    }

    return pd.read_csv(file_path, dtype=usable_dtypes)


@st.cache_data(show_spinner=False)
def load_customer_segments_optimized():

    dtype_map = {
        "CustomerID": "int32",
        "Cluster": "int8",
        "CustomerSegment": "category",
        "Country": "category",
        "Recency": "int32",
        "Frequency": "int32",
        "Monetary": "float32",
        "AvgRevenue": "float32",
        "UniqueProducts": "int32",
    }

    file_path = PROCESSED_DATA_DIR / "customer_segments.csv"

    header_columns = pd.read_csv(file_path, nrows=0).columns.tolist()

    usable_dtypes = {
        column: dtype
        for column, dtype in dtype_map.items()
        if column in header_columns
    }

    return pd.read_csv(file_path, dtype=usable_dtypes)


sales_df = load_sales_data()

customer_df = load_customer_features_optimized()

segment_df = load_customer_segments_optimized()

# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("📊 Business Insights")

st.markdown(
    """
An executive summary of sales performance, customer value, product
performance, and recommended next steps — all computed from this
project's own processed data.
"""
)

st.divider()

# ==========================================================
# EXECUTIVE KPI OVERVIEW
# ==========================================================

st.header("📌 Executive KPI Overview")

total_revenue = sales_df["Revenue"].sum()

total_customers = sales_df["CustomerID"].nunique()

total_products = sales_df["StockCode"].nunique()

total_orders = sales_df["InvoiceNo"].nunique()

total_countries = sales_df["Country"].nunique()

avg_order_value = total_revenue / total_orders

avg_customer_value = customer_df["Monetary"].mean()

total_segments = segment_df["CustomerSegment"].nunique()

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Revenue",
        format_currency(total_revenue),
    )

with k2:

    st.metric(
        "Customers",
        f"{total_customers:,}",
    )

with k3:

    st.metric(
        "Products",
        f"{total_products:,}",
    )

with k4:

    st.metric(
        "Orders",
        f"{total_orders:,}",
    )

k5, k6, k7, k8 = st.columns(4)

with k5:

    st.metric(
        "Countries",
        f"{total_countries:,}",
    )

with k6:

    st.metric(
        "Avg Order Value",
        format_currency(avg_order_value),
    )

with k7:

    st.metric(
        "Avg Customer Value",
        format_currency(avg_customer_value),
    )

with k8:

    st.metric(
        "Customer Segments",
        total_segments,
    )

st.divider()

# ==========================================================
# REVENUE TREND
# ==========================================================

st.header("📈 Revenue Trend")

st.caption("Total revenue booked in each calendar month.")

monthly_revenue = (
    sales_df.groupby(["Year", "Month", "MonthName"], as_index=False)["Revenue"]
    .sum()
    .sort_values(["Year", "Month"])
)

monthly_revenue["Period"] = (
    monthly_revenue["MonthName"].str[:3]
    + " "
    + monthly_revenue["Year"].astype(str)
)

fig_monthly_revenue = px.line(
    monthly_revenue,
    x="Period",
    y="Revenue",
    markers=True,
    template="plotly_dark",
)

fig_monthly_revenue.update_layout(
    height=380,
    margin=dict(l=10, r=10, t=10, b=10),
)

st.plotly_chart(
    fig_monthly_revenue,
    use_container_width=True,
)

st.divider()

# ==========================================================
# REVENUE BY SEGMENT + TOP COUNTRIES
# ==========================================================

st.header("💰 Revenue by Segment & Market")

seg_left, seg_right = st.columns(2)

with seg_left:

    st.subheader("Revenue Contribution by Segment")

    segment_revenue = (
        segment_df.groupby("CustomerSegment", as_index=False)["Monetary"]
        .sum()
    )

    fig_segment_pie = px.pie(
        segment_revenue,
        names="CustomerSegment",
        values="Monetary",
        hole=0.45,
        template="plotly_dark",
    )

    fig_segment_pie.update_layout(
        height=380,
        margin=dict(l=10, r=10, t=10, b=10),
    )

    st.plotly_chart(
        fig_segment_pie,
        use_container_width=True,
    )

with seg_right:

    st.subheader("Top 10 Countries by Revenue")

    top_countries = (
        sales_df.groupby("Country", as_index=False)["Revenue"]
        .sum()
        .sort_values("Revenue", ascending=False)
        .head(10)
    )

    fig_top_countries = px.bar(
        top_countries,
        x="Revenue",
        y="Country",
        orientation="h",
        template="plotly_dark",
    )

    fig_top_countries.update_layout(
        height=380,
        yaxis=dict(autorange="reversed"),
        margin=dict(l=10, r=10, t=10, b=10),
    )

    st.plotly_chart(
        fig_top_countries,
        use_container_width=True,
    )

st.divider()

# ==========================================================
# CUSTOMER INSIGHTS
# ==========================================================

st.header("👥 Customer Insights")

customer_summary = pd.DataFrame(
    {
        "Metric": [
            "Customers",
            "Average Frequency",
            "Average Monetary",
            "Average Revenue",
            "Average Unique Products",
        ],
        "Value": [
            customer_df["CustomerID"].nunique(),
            round(customer_df["Frequency"].mean(), 2),
            round(customer_df["Monetary"].mean(), 2),
            round(customer_df["AvgRevenue"].mean(), 2),
            round(customer_df["UniqueProducts"].mean(), 2),
        ],
    }
)

cust_left, cust_right = st.columns([1, 1.3])

with cust_left:

    st.dataframe(
        customer_summary,
        use_container_width=True,
        hide_index=True,
    )

with cust_right:

    fig_customer_hist = px.histogram(
        customer_df,
        x="Monetary",
        nbins=40,
        template="plotly_dark",
        title="Customer Monetary Value Distribution",
    )

    fig_customer_hist.update_layout(
        height=320,
        margin=dict(l=10, r=10, t=40, b=10),
    )

    st.plotly_chart(
        fig_customer_hist,
        use_container_width=True,
    )

st.divider()

# ==========================================================
# TOP CUSTOMERS
# ==========================================================

st.header("🏅 Top 20 Customers by Value")

top_customers = (
    customer_df.sort_values("Monetary", ascending=False)
    .head(20)
)

fig_top_customers = px.bar(
    top_customers,
    x="Monetary",
    y=top_customers["CustomerID"].astype(str),
    orientation="h",
    template="plotly_dark",
)

fig_top_customers.update_layout(
    height=480,
    yaxis=dict(
        autorange="reversed",
        title="Customer ID",
    ),
    margin=dict(l=10, r=10, t=10, b=10),
)

st.plotly_chart(
    fig_top_customers,
    use_container_width=True,
)

st.dataframe(
    top_customers[
        [
            "CustomerID",
            "Country",
            "Frequency",
            "Monetary",
            "AvgRevenue",
            "UniqueProducts",
        ]
    ],
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# CUSTOMER SEGMENTS
# ==========================================================

st.header("🎯 Customer Segments")

segment_summary = (
    segment_df.groupby("CustomerSegment", as_index=False)
    .agg(
        Customers=("CustomerID", "count"),
        AvgRevenue=("AvgRevenue", "mean"),
        AvgMonetary=("Monetary", "mean"),
        AvgFrequency=("Frequency", "mean"),
    )
    .round(2)
    .sort_values("AvgMonetary", ascending=False)
)

fig_segment_bar = px.bar(
    segment_summary,
    x="CustomerSegment",
    y="AvgMonetary",
    color="CustomerSegment",
    template="plotly_dark",
    title="Average Monetary Value by Segment",
)

fig_segment_bar.update_layout(
    height=360,
    showlegend=False,
    margin=dict(l=10, r=10, t=40, b=10),
)

st.plotly_chart(
    fig_segment_bar,
    use_container_width=True,
)

st.dataframe(
    segment_summary,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# PRODUCT INSIGHTS
# ==========================================================

st.header("📦 Product Insights")

product_summary = (
    sales_df.groupby(["StockCode", "Description"], as_index=False)
    .agg(
        Orders=("InvoiceNo", "nunique"),
        Quantity=("Quantity", "sum"),
        Revenue=("Revenue", "sum"),
        Customers=("CustomerID", "nunique"),
    )
    .sort_values("Revenue", ascending=False)
)

prod_left, prod_right = st.columns(2)

with prod_left:

    st.subheader("Top 10 Products by Revenue")

    fig_top_products_revenue = px.bar(
        product_summary.head(10),
        x="Revenue",
        y="Description",
        orientation="h",
        template="plotly_dark",
    )

    fig_top_products_revenue.update_layout(
        height=400,
        yaxis=dict(autorange="reversed"),
        margin=dict(l=10, r=10, t=10, b=10),
    )

    st.plotly_chart(
        fig_top_products_revenue,
        use_container_width=True,
    )

with prod_right:

    st.subheader("Top 10 Best-Selling Products")

    best_selling = (
        product_summary.sort_values("Quantity", ascending=False)
        .head(10)
    )

    fig_best_selling = px.bar(
        best_selling,
        x="Quantity",
        y="Description",
        orientation="h",
        template="plotly_dark",
    )

    fig_best_selling.update_layout(
        height=400,
        yaxis=dict(autorange="reversed"),
        margin=dict(l=10, r=10, t=10, b=10),
    )

    st.plotly_chart(
        fig_best_selling,
        use_container_width=True,
    )

st.divider()

# ==========================================================
# PRODUCT PERFORMANCE SUMMARY
# ==========================================================

st.header("📈 Product Performance Summary")

performance = pd.DataFrame(
    {
        "Metric": [
            "Unique Products",
            "Average Revenue per Order Line",
            "Average Quantity per Order Line",
            "Maximum Revenue (single line item)",
            "Maximum Quantity (single line item)",
        ],
        "Value": [
            sales_df["StockCode"].nunique(),
            round(sales_df["Revenue"].mean(), 2),
            round(sales_df["Quantity"].mean(), 2),
            round(sales_df["Revenue"].max(), 2),
            round(sales_df["Quantity"].max(), 2),
        ],
    }
)

st.dataframe(
    performance,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# REVENUE SHARE (TREEMAP)
# ==========================================================

st.header("🧩 Revenue Share by Product")

st.caption("Each block represents a product — larger blocks generated more revenue.")

treemap_products = product_summary.head(30)

fig_treemap = px.treemap(
    treemap_products,
    path=["Description"],
    values="Revenue",
    template="plotly_dark",
)

fig_treemap.update_layout(
    height=450,
    margin=dict(l=10, r=10, t=10, b=10),
)

st.plotly_chart(
    fig_treemap,
    use_container_width=True,
)

st.divider()

# ==========================================================
# PRODUCT SEARCH
# ==========================================================

st.header("🔍 Product Search")

product_search = st.text_input("Search a product by name or keyword")

if product_search:

    product_results = product_summary[
        product_summary["Description"].str.contains(
            product_search,
            case=False,
            na=False,
        )
    ]

    st.success(f"{len(product_results):,} products matched.")

    st.dataframe(
        product_results,
        use_container_width=True,
        hide_index=True,
    )

st.divider()

# ==========================================================
# COUNTRY INSIGHTS
# ==========================================================

st.header("🌍 Country Insights")

country_performance = (
    sales_df.groupby("Country", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Orders=("InvoiceNo", "nunique"),
        Customers=("CustomerID", "nunique"),
        Quantity=("Quantity", "sum"),
    )
    .sort_values("Revenue", ascending=False)
)

country_left, country_right = st.columns([1.3, 1])

with country_left:

    fig_country_performance = px.bar(
        country_performance.head(10),
        x="Revenue",
        y="Country",
        orientation="h",
        template="plotly_dark",
        title="Top 10 Revenue-Generating Countries",
    )

    fig_country_performance.update_layout(
        height=420,
        yaxis=dict(autorange="reversed"),
        margin=dict(l=10, r=10, t=40, b=10),
    )

    st.plotly_chart(
        fig_country_performance,
        use_container_width=True,
    )

with country_right:

    st.dataframe(
        country_performance.head(10),
        use_container_width=True,
        hide_index=True,
    )

st.divider()

# ==========================================================
# COUNTRY SEARCH
# ==========================================================

st.header("🔍 Country Explorer")

selected_country = st.selectbox(
    "View a country's numbers",
    sorted(sales_df["Country"].unique()),
)

country_data = sales_df[sales_df["Country"] == selected_country]

cn1, cn2, cn3, cn4 = st.columns(4)

with cn1:

    st.metric(
        "Revenue",
        format_currency(country_data["Revenue"].sum()),
    )

with cn2:

    st.metric(
        "Customers",
        f"{country_data['CustomerID'].nunique():,}",
    )

with cn3:

    st.metric(
        "Orders",
        f"{country_data['InvoiceNo'].nunique():,}",
    )

with cn4:

    st.metric(
        "Products Sold",
        f"{country_data['StockCode'].nunique():,}",
    )

country_top_products = (
    country_data.groupby("Description", as_index=False)["Revenue"]
    .sum()
    .sort_values("Revenue", ascending=False)
    .head(5)
)

fig_country_products = px.bar(
    country_top_products,
    x="Revenue",
    y="Description",
    orientation="h",
    template="plotly_dark",
    title=f"Top 5 Products in {selected_country}",
)

fig_country_products.update_layout(
    height=320,
    yaxis=dict(autorange="reversed"),
    margin=dict(l=10, r=10, t=40, b=10),
)

st.plotly_chart(
    fig_country_products,
    use_container_width=True,
)

st.divider()

# ==========================================================
# EXECUTIVE KPI TABLE
# ==========================================================

st.header("🏆 Executive KPI Table")

executive_table = pd.DataFrame(
    {
        "KPI": [
            "Total Revenue",
            "Total Customers",
            "Total Products",
            "Total Orders",
            "Total Countries",
            "Average Order Value",
            "Average Customer Value",
        ],
        "Value": [
            format_currency(total_revenue),
            f"{total_customers:,}",
            f"{total_products:,}",
            f"{total_orders:,}",
            f"{total_countries:,}",
            format_currency(avg_order_value),
            format_currency(avg_customer_value),
        ],
    }
)

st.dataframe(
    executive_table,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# BUSINESS HEALTH SUMMARY
# ==========================================================

st.header("🏥 Business Health Summary")

health_left, health_mid, health_right = st.columns(3)

top_segment_share = (
    segment_revenue.sort_values("Monetary", ascending=False).iloc[0]["Monetary"]
    / segment_revenue["Monetary"].sum()
    * 100
)

top_country_share = (
    country_performance.iloc[0]["Revenue"]
    / country_performance["Revenue"].sum()
    * 100
)

top_product_share = (
    product_summary.iloc[0]["Revenue"]
    / product_summary["Revenue"].sum()
    * 100
)

with health_left:

    st.metric(
        "Top Segment's Revenue Share",
        f"{top_segment_share:.1f}%",
    )

with health_mid:

    st.metric(
        "Top Country's Revenue Share",
        f"{top_country_share:.1f}%",
    )

with health_right:

    st.metric(
        "Top Product's Revenue Share",
        f"{top_product_share:.1f}%",
    )

if top_country_share > 50:

    st.warning(
        f"Revenue is heavily concentrated in one country "
        f"({country_performance.iloc[0]['Country']}, {top_country_share:.1f}% "
        f"of total revenue). Consider diversifying into other markets."
    )

else:

    st.success(
        "Revenue is reasonably diversified across countries."
    )

st.divider()

# ==========================================================
# STRATEGIC BUSINESS RECOMMENDATIONS
# ==========================================================

st.header("🚀 Strategic Recommendations")

rec_left, rec_mid, rec_right = st.columns(3)

with rec_left:

    st.success(
        """
**Retention**

- Focus loyalty programs on the highest-revenue segments
- Prioritize customer service for top-spending customers
- Monitor recency trends for early churn signals
"""
    )

with rec_mid:

    st.info(
        """
**Growth**

- Cross-sell top-performing products to medium-value customers
- Bundle best-sellers with slower-moving inventory
- Expand marketing in high-performing countries
"""
    )

with rec_right:

    st.warning(
        """
**Recovery**

- Run win-back campaigns in lower-performing regions
- Re-engage customers with declining purchase frequency
- Review pricing or assortment in weaker markets
"""
    )

st.divider()

# ==========================================================
# INTERACTIVE FILTERS
# ==========================================================

st.header("🎛 Interactive Filters")

filter_col1, filter_col2 = st.columns(2)

with filter_col1:

    filter_country = st.selectbox(
        "Country",
        ["All"] + sorted(sales_df["Country"].unique().tolist()),
        key="bi_filter_country",
    )

with filter_col2:

    filter_year = st.selectbox(
        "Year",
        ["All"] + sorted(sales_df["Year"].unique().tolist()),
        key="bi_filter_year",
    )

filtered_df = sales_df.copy()

if filter_country != "All":

    filtered_df = filtered_df[filtered_df["Country"] == filter_country]

if filter_year != "All":

    filtered_df = filtered_df[filtered_df["Year"] == filter_year]

st.success(f"{len(filtered_df):,} rows selected.")

filter_kpi1, filter_kpi2, filter_kpi3, filter_kpi4 = st.columns(4)

with filter_kpi1:

    st.metric(
        "Revenue",
        format_currency(filtered_df["Revenue"].sum()),
    )

with filter_kpi2:

    st.metric(
        "Customers",
        f"{filtered_df['CustomerID'].nunique():,}",
    )

with filter_kpi3:

    st.metric(
        "Orders",
        f"{filtered_df['InvoiceNo'].nunique():,}",
    )

with filter_kpi4:

    st.metric(
        "Products",
        f"{filtered_df['StockCode'].nunique():,}",
    )

st.dataframe(
    filtered_df.head(200),
    use_container_width=True,
    hide_index=True,
)

download_csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Filtered Sales Data",
    data=download_csv,
    file_name="filtered_business_insights.csv",
    mime="text/csv",
)

st.divider()

# ==========================================================
# KEY OBSERVATIONS (COMPUTED FROM THIS DATASET)
# ==========================================================

st.header("📌 Key Observations")

st.caption(
    "These insights are computed live from the data above - nothing here is hardcoded."
)

best_segment_row = segment_summary.iloc[0]

best_country_row = country_performance.iloc[0]

best_product_row = product_summary.iloc[0]

obs1, obs2 = st.columns(2)

with obs1:

    st.info(
        f"**Top-performing segment:** {best_segment_row['CustomerSegment']} "
        f"has the highest average monetary value, at "
        f"{format_currency(best_segment_row['AvgMonetary'])}."
    )

    st.info(
        f"**Top market:** {best_country_row['Country']} leads with "
        f"{format_currency(best_country_row['Revenue'])} in revenue, "
        f"{top_country_share:.1f}% of the total."
    )

with obs2:

    st.info(
        f"**Top product:** \"{best_product_row['Description']}\" is the "
        f"highest revenue-generating product, at "
        f"{format_currency(best_product_row['Revenue'])}."
    )

    st.info(
        f"**Average order value:** Each order is worth "
        f"{format_currency(avg_order_value)} on average, across "
        f"{total_orders:,} orders."
    )

st.divider()

# ==========================================================
# NAVIGATION
# ==========================================================

nav_left, nav_right = st.columns(2)

with nav_left:

    st.caption("⬅ Previous Page: Recommendation System")

with nav_right:

    st.caption("➡ Next Page: About")