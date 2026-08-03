"""
Data Overview Page
-------------------------------------------------------------

This page gives a complete, visual walkthrough of the cleaned
Online Retail dataset that powers every other page in this
dashboard (Customer Segmentation, CLV Prediction, Churn
Prediction, Recommendation System, and Business Insights).

Everything shown on this page - every number, chart, and table -
is computed directly from `final_cleaned_dataset.csv`, using the
same `load_cleaned_data()` loader used throughout the project.
No external data, images, or text is used anywhere on this page.

Author: Arin Bhardwaj
Project: Intelligent Customer Analytics Platform
"""

import pandas as pd
import plotly.express as px
import streamlit as st

from utils.data_loader import load_cleaned_data
from utils.helper import format_currency, format_number

# ==========================================================
# LOAD DATA (WITH A CLEAR DIAGNOSTIC IF SOMETHING'S WRONG)
# ==========================================================
#
# If this fails, it is almost always a deployment issue, not a
# bug in this page: either the processed CSV files were not
# committed to the repository, they exceed a hosting size limit,
# or they are tracked with Git LFS (which Streamlit Cloud does
# not fetch by default, leaving only a small pointer file behind
# instead of the real data).

REQUIRED_COLUMNS = [
    "CustomerID",
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "Revenue",
    "Country",
    "Year",
    "Month",
    "MonthName",
    "DayName",
    "TimeOfDay",
    "IsWeekend",
]

try:

    df = load_cleaned_data()

except FileNotFoundError:

    st.error(
        "**Could not find `final_cleaned_dataset.csv`.**\n\n"
        "This usually means the `data/processed/` folder was not "
        "deployed with the app — check that it's committed to your "
        "repository, isn't excluded by `.gitignore`, and isn't over "
        "your hosting provider's file size limit (Git LFS files in "
        "particular are not fetched by Streamlit Cloud by default)."
    )

    st.stop()

missing_columns = [
    column for column in REQUIRED_COLUMNS if column not in df.columns
]

if missing_columns:

    st.error(
        f"**The dataset was loaded, but is missing expected columns: "
        f"{', '.join(missing_columns)}.**\n\n"
        f"This almost always means the file that was loaded isn't the "
        f"real dataset — for example, a Git LFS pointer file being "
        f"read instead of the actual CSV. Found columns instead: "
        f"{', '.join(df.columns.tolist())}."
    )

    st.stop()

DAY_ORDER = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("📊 Data Overview")

st.markdown(
    """
This page explores the processed **Online Retail dataset** that
feeds every model and dashboard in this platform.

Use the KPIs, charts, and explorers below to understand the shape
of the data, where the revenue comes from, who the customers are,
and when they shop.
"""
)

st.divider()

# ==========================================================
# DATASET SCALE - KPI OVERVIEW
# ==========================================================

st.header("📌 Dataset at a Glance")

total_rows = len(df)

total_columns = len(df.columns)

total_customers = df["CustomerID"].nunique()

total_transactions = df["InvoiceNo"].nunique()

total_products = df["StockCode"].nunique()

total_countries = df["Country"].nunique()

total_revenue = df["Revenue"].sum()

total_quantity = int(df["Quantity"].sum())

avg_order_value = total_revenue / total_transactions

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Rows",
        f"{total_rows:,}",
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
        "Countries",
        f"{total_countries:,}",
    )

k5, k6, k7, k8 = st.columns(4)

with k5:

    st.metric(
        "Transactions",
        f"{total_transactions:,}",
    )

with k6:

    st.metric(
        "Total Quantity Sold",
        format_number(total_quantity),
    )

with k7:

    st.metric(
        "Total Revenue",
        format_currency(total_revenue),
    )

with k8:

    st.metric(
        "Avg Order Value",
        format_currency(avg_order_value),
    )

st.divider()

# ==========================================================
# DATASET PREVIEW
# ==========================================================

st.header("👀 Dataset Preview")

st.caption(
    "A live sample of the cleaned dataset. Use the slider to see more or fewer rows."
)

rows_to_show = st.slider(
    "Number of rows to preview",
    min_value=5,
    max_value=100,
    value=10,
    step=5,
)

st.dataframe(
    df.head(rows_to_show),
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# COLUMN REFERENCE TABLE
# ==========================================================

st.header("📋 Column Reference")

st.caption(
    "Every column used across this dashboard, with its data type and number of unique values."
)

column_reference = pd.DataFrame(
    {
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str).values,
        "Unique Values": df.nunique().values,
    }
)

st.dataframe(
    column_reference,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# REVENUE & QUANTITY DISTRIBUTION
# ==========================================================

st.header("💵 Revenue & Quantity Distribution")

dist_left, dist_right = st.columns(2)

with dist_left:

    st.subheader("Revenue per Line Item")

    revenue_stats = (
        df["Revenue"]
        .describe(percentiles=[0.25, 0.5, 0.75, 0.90])
        .to_frame(name="Revenue")
        .round(2)
    )

    st.dataframe(
        revenue_stats,
        use_container_width=True,
    )

with dist_right:

    st.subheader("Quantity per Line Item")

    quantity_stats = (
        df["Quantity"]
        .describe(percentiles=[0.25, 0.5, 0.75, 0.90])
        .to_frame(name="Quantity")
        .round(2)
    )

    st.dataframe(
        quantity_stats,
        use_container_width=True,
    )

st.divider()

# ==========================================================
# MONTHLY REVENUE TREND
# ==========================================================

st.header("📈 Monthly Revenue Trend")

st.caption("Total revenue booked in each calendar month across the dataset.")

monthly_sales = (
    df.groupby(["Year", "Month", "MonthName"], as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Quantity=("Quantity", "sum"),
        Transactions=("InvoiceNo", "nunique"),
    )
    .sort_values(["Year", "Month"])
)

monthly_sales["Period"] = (
    monthly_sales["MonthName"].str[:3]
    + " "
    + monthly_sales["Year"].astype(str)
)

fig_monthly_revenue = px.line(
    monthly_sales,
    x="Period",
    y="Revenue",
    markers=True,
    template="plotly_dark",
    title="Total Revenue by Month",
)

fig_monthly_revenue.update_layout(
    height=380,
    margin=dict(l=10, r=10, t=40, b=10),
)

st.plotly_chart(
    fig_monthly_revenue,
    use_container_width=True,
)

st.divider()

# ==========================================================
# MONTHLY QUANTITY TREND
# ==========================================================

st.header("📦 Monthly Quantity Trend")

st.caption("Total units sold in each calendar month across the dataset.")

fig_monthly_quantity = px.bar(
    monthly_sales,
    x="Period",
    y="Quantity",
    template="plotly_dark",
    title="Total Quantity Sold by Month",
)

fig_monthly_quantity.update_layout(
    height=380,
    margin=dict(l=10, r=10, t=40, b=10),
)

st.plotly_chart(
    fig_monthly_quantity,
    use_container_width=True,
)

st.divider()

# ==========================================================
# YEAR-OVER-YEAR COMPARISON
# ==========================================================

st.header("📆 Year-over-Year Comparison")

yearly_summary = (
    df.groupby("Year", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Transactions=("InvoiceNo", "nunique"),
        Customers=("CustomerID", "nunique"),
    )
)

y_left, y_right = st.columns([1, 1])

with y_left:

    fig_yearly_revenue = px.bar(
        yearly_summary,
        x="Year",
        y="Revenue",
        template="plotly_dark",
        title="Revenue by Year",
    )

    fig_yearly_revenue.update_layout(
        height=340,
        margin=dict(l=10, r=10, t=40, b=10),
    )

    st.plotly_chart(
        fig_yearly_revenue,
        use_container_width=True,
    )

with y_right:

    st.dataframe(
        yearly_summary,
        use_container_width=True,
        hide_index=True,
    )

st.divider()

# ==========================================================
# TOP COUNTRIES BY REVENUE
# ==========================================================

st.header("🌍 Top Countries by Revenue")

country_summary = (
    df.groupby("Country", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Quantity=("Quantity", "sum"),
        Customers=("CustomerID", "nunique"),
        Transactions=("InvoiceNo", "nunique"),
    )
    .sort_values("Revenue", ascending=False)
)

top_countries = country_summary.head(10)

country_left, country_right = st.columns([1.3, 1])

with country_left:

    fig_top_countries = px.bar(
        top_countries,
        x="Revenue",
        y="Country",
        orientation="h",
        template="plotly_dark",
        title="Top 10 Countries by Revenue",
    )

    fig_top_countries.update_layout(
        height=420,
        yaxis=dict(autorange="reversed"),
        margin=dict(l=10, r=10, t=40, b=10),
    )

    st.plotly_chart(
        fig_top_countries,
        use_container_width=True,
    )

with country_right:

    fig_country_share = px.pie(
        top_countries,
        names="Country",
        values="Revenue",
        hole=0.45,
        template="plotly_dark",
        title="Revenue Share (Top 10)",
    )

    fig_country_share.update_layout(
        height=420,
        margin=dict(l=10, r=10, t=40, b=10),
    )

    st.plotly_chart(
        fig_country_share,
        use_container_width=True,
    )

st.divider()

# ==========================================================
# TOP PRODUCTS BY REVENUE AND QUANTITY
# ==========================================================

st.header("🏆 Top Products")

product_summary = (
    df.groupby(["StockCode", "Description"], as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Quantity=("Quantity", "sum"),
    )
)

product_left, product_right = st.columns(2)

with product_left:

    st.subheader("By Revenue")

    top_products_revenue = (
        product_summary
        .sort_values("Revenue", ascending=False)
        .head(10)
    )

    fig_top_products_revenue = px.bar(
        top_products_revenue,
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

with product_right:

    st.subheader("By Quantity Sold")

    top_products_quantity = (
        product_summary
        .sort_values("Quantity", ascending=False)
        .head(10)
    )

    fig_top_products_quantity = px.bar(
        top_products_quantity,
        x="Quantity",
        y="Description",
        orientation="h",
        template="plotly_dark",
    )

    fig_top_products_quantity.update_layout(
        height=400,
        yaxis=dict(autorange="reversed"),
        margin=dict(l=10, r=10, t=10, b=10),
    )

    st.plotly_chart(
        fig_top_products_quantity,
        use_container_width=True,
    )

st.divider()

# ==========================================================
# REVENUE SHARE BY PRODUCT (TREEMAP)
# ==========================================================

st.header("🧩 Revenue Share by Product")

st.caption("Each block represents a product - larger blocks generated more revenue.")

treemap_products = (
    product_summary
    .sort_values("Revenue", ascending=False)
    .head(30)
)

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
# TOP CUSTOMERS BY REVENUE
# ==========================================================

st.header("👥 Top Customers by Revenue")

customer_summary = (
    df.groupby("CustomerID", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Transactions=("InvoiceNo", "nunique"),
        Quantity=("Quantity", "sum"),
    )
)

top_customers = (
    customer_summary
    .sort_values("Revenue", ascending=False)
    .head(10)
)

cust_left, cust_right = st.columns([1.3, 1])

with cust_left:

    fig_top_customers = px.bar(
        top_customers,
        x="Revenue",
        y=top_customers["CustomerID"].astype(str),
        orientation="h",
        template="plotly_dark",
        title="Top 10 Customers by Revenue",
    )

    fig_top_customers.update_layout(
        height=380,
        yaxis=dict(
            autorange="reversed",
            title="Customer ID",
        ),
        margin=dict(l=10, r=10, t=40, b=10),
    )

    st.plotly_chart(
        fig_top_customers,
        use_container_width=True,
    )

with cust_right:

    st.subheader("Revenue Spread Across Customers")

    fig_customer_hist = px.histogram(
        customer_summary,
        x="Revenue",
        nbins=40,
        template="plotly_dark",
    )

    fig_customer_hist.update_layout(
        height=380,
        margin=dict(l=10, r=10, t=10, b=10),
    )

    st.plotly_chart(
        fig_customer_hist,
        use_container_width=True,
    )

st.divider()

# ==========================================================
# DAY OF WEEK ANALYSIS
# ==========================================================

st.header("📅 Sales by Day of the Week")

day_summary = (
    df.groupby("DayName", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Transactions=("InvoiceNo", "nunique"),
        Customers=("CustomerID", "nunique"),
    )
)

day_summary["DayName"] = pd.Categorical(
    day_summary["DayName"],
    categories=DAY_ORDER,
    ordered=True,
)

day_summary = day_summary.sort_values("DayName")

fig_day = px.bar(
    day_summary,
    x="DayName",
    y="Revenue",
    template="plotly_dark",
    title="Revenue by Day of the Week",
)

fig_day.update_layout(
    height=360,
    margin=dict(l=10, r=10, t=40, b=10),
)

st.plotly_chart(
    fig_day,
    use_container_width=True,
)

st.divider()

# ==========================================================
# TIME OF DAY ANALYSIS
# ==========================================================

st.header("🕒 Sales by Time of Day")

time_summary = (
    df.groupby("TimeOfDay", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Transactions=("InvoiceNo", "nunique"),
        Customers=("CustomerID", "nunique"),
    )
)

time_left, time_right = st.columns([1, 1.3])

with time_left:

    fig_time_pie = px.pie(
        time_summary,
        names="TimeOfDay",
        values="Revenue",
        hole=0.45,
        template="plotly_dark",
        title="Revenue Share by Time of Day",
    )

    fig_time_pie.update_layout(
        height=360,
        margin=dict(l=10, r=10, t=40, b=10),
    )

    st.plotly_chart(
        fig_time_pie,
        use_container_width=True,
    )

with time_right:

    st.dataframe(
        time_summary,
        use_container_width=True,
        hide_index=True,
    )

st.divider()

# ==========================================================
# WEEKDAY VS WEEKEND
# ==========================================================

st.header("📊 Weekday vs Weekend")

weekend_summary = (
    df.groupby("IsWeekend", as_index=False)
    .agg(
        Revenue=("Revenue", "sum"),
        Transactions=("InvoiceNo", "nunique"),
        Customers=("CustomerID", "nunique"),
    )
)

weekend_summary["Purchase Type"] = weekend_summary["IsWeekend"].map(
    {
        False: "Weekday",
        True: "Weekend",
    }
)

weekend_left, weekend_right = st.columns([1.3, 1])

with weekend_left:

    fig_weekend = px.bar(
        weekend_summary,
        x="Purchase Type",
        y="Revenue",
        color="Purchase Type",
        template="plotly_dark",
        title="Revenue: Weekday vs Weekend",
    )

    fig_weekend.update_layout(
        height=360,
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
    )

    st.plotly_chart(
        fig_weekend,
        use_container_width=True,
    )

with weekend_right:

    st.dataframe(
        weekend_summary[
            [
                "Purchase Type",
                "Revenue",
                "Transactions",
                "Customers",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )

st.divider()

# ==========================================================
# DAY x TIME OF DAY HEATMAP
# ==========================================================

st.header("🔥 Revenue Heatmap — Day of Week vs Time of Day")

st.caption(
    "Darker cells mean more revenue was generated in that day / time-of-day combination."
)

heatmap_data = (
    df.groupby(["DayName", "TimeOfDay"], as_index=False)["Revenue"]
    .sum()
)

heatmap_pivot = heatmap_data.pivot(
    index="DayName",
    columns="TimeOfDay",
    values="Revenue",
).reindex(DAY_ORDER)

fig_heatmap = px.imshow(
    heatmap_pivot,
    text_auto=".2s",
    aspect="auto",
    template="plotly_dark",
    color_continuous_scale="Blues",
)

fig_heatmap.update_layout(
    height=400,
    margin=dict(l=10, r=10, t=10, b=10),
)

st.plotly_chart(
    fig_heatmap,
    use_container_width=True,
)

st.divider()

# ==========================================================
# COUNTRY EXPLORER
# ==========================================================

st.header("🔍 Country Explorer")

selected_country = st.selectbox(
    "Select a Country",
    sorted(df["Country"].unique()),
)

country_df = df[df["Country"] == selected_country]

ce1, ce2, ce3, ce4 = st.columns(4)

with ce1:

    st.metric(
        "Customers",
        f"{country_df['CustomerID'].nunique():,}",
    )

with ce2:

    st.metric(
        "Transactions",
        f"{country_df['InvoiceNo'].nunique():,}",
    )

with ce3:

    st.metric(
        "Products",
        f"{country_df['StockCode'].nunique():,}",
    )

with ce4:

    st.metric(
        "Revenue",
        format_currency(country_df["Revenue"].sum()),
    )

country_top_products = (
    country_df.groupby("Description", as_index=False)["Revenue"]
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
# YEAR EXPLORER
# ==========================================================

st.header("📆 Year Explorer")

selected_year = st.selectbox(
    "Select a Year",
    sorted(df["Year"].unique()),
)

year_df = df[df["Year"] == selected_year]

ye1, ye2, ye3, ye4 = st.columns(4)

with ye1:

    st.metric(
        "Revenue",
        format_currency(year_df["Revenue"].sum()),
    )

with ye2:

    st.metric(
        "Transactions",
        f"{year_df['InvoiceNo'].nunique():,}",
    )

with ye3:

    st.metric(
        "Customers",
        f"{year_df['CustomerID'].nunique():,}",
    )

with ye4:

    st.metric(
        "Products",
        f"{year_df['StockCode'].nunique():,}",
    )

year_monthly = (
    year_df.groupby(["Month", "MonthName"], as_index=False)["Revenue"]
    .sum()
    .sort_values("Month")
)

fig_year_monthly = px.bar(
    year_monthly,
    x="MonthName",
    y="Revenue",
    template="plotly_dark",
    title=f"Monthly Revenue in {selected_year}",
)

fig_year_monthly.update_layout(
    height=340,
    margin=dict(l=10, r=10, t=40, b=10),
)

st.plotly_chart(
    fig_year_monthly,
    use_container_width=True,
)

st.divider()

# ==========================================================
# INTERACTIVE MULTI-FILTER EXPLORER
# ==========================================================

st.header("🎛 Interactive Dataset Filters")

st.caption(
    "Combine filters to drill into any slice of the dataset, then download the result."
)

filter_col1, filter_col2, filter_col3 = st.columns(3)

with filter_col1:

    filter_country = st.selectbox(
        "Country",
        ["All"] + sorted(df["Country"].unique().tolist()),
        key="filter_country",
    )

with filter_col2:

    filter_year = st.selectbox(
        "Year",
        ["All"] + sorted(df["Year"].unique().tolist()),
        key="filter_year",
    )

with filter_col3:

    filter_weekend = st.selectbox(
        "Purchase Type",
        ["All", "Weekday", "Weekend"],
        key="filter_weekend",
    )

filtered_df = df.copy()

if filter_country != "All":

    filtered_df = filtered_df[filtered_df["Country"] == filter_country]

if filter_year != "All":

    filtered_df = filtered_df[filtered_df["Year"] == filter_year]

if filter_weekend != "All":

    filtered_df = filtered_df[
        filtered_df["IsWeekend"] == (filter_weekend == "Weekend")
    ]

st.success(f"Filtered Dataset: {len(filtered_df):,} rows")

filter_kpi1, filter_kpi2, filter_kpi3, filter_kpi4 = st.columns(4)

with filter_kpi1:

    st.metric(
        "Customers",
        f"{filtered_df['CustomerID'].nunique():,}",
    )

with filter_kpi2:

    st.metric(
        "Transactions",
        f"{filtered_df['InvoiceNo'].nunique():,}",
    )

with filter_kpi3:

    st.metric(
        "Products",
        f"{filtered_df['StockCode'].nunique():,}",
    )

with filter_kpi4:

    st.metric(
        "Revenue",
        format_currency(filtered_df["Revenue"].sum()),
    )

st.dataframe(
    filtered_df.head(200),
    use_container_width=True,
    hide_index=True,
)

download_csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Dataset",
    data=download_csv,
    file_name="filtered_online_retail.csv",
    mime="text/csv",
)

st.divider()

# ==========================================================
# KEY OBSERVATIONS (COMPUTED FROM THIS DATASET)
# ==========================================================

st.header("📌 Key Observations")

st.caption("These insights are computed live from the dataset above - nothing here is hardcoded.")

best_month_row = monthly_sales.sort_values("Revenue", ascending=False).iloc[0]

best_country_row = country_summary.iloc[0]

best_product_row = product_summary.sort_values("Revenue", ascending=False).iloc[0]

best_day_row = day_summary.sort_values("Revenue", ascending=False).iloc[0]

weekend_share = (
    weekend_summary.loc[weekend_summary["Purchase Type"] == "Weekend", "Revenue"].sum()
    / weekend_summary["Revenue"].sum()
    * 100
)

obs1, obs2 = st.columns(2)

with obs1:

    st.info(
        f"**Best-performing month:** {best_month_row['Period']} "
        f"generated {format_currency(best_month_row['Revenue'])} in revenue."
    )

    st.info(
        f"**Top market:** {best_country_row['Country']} leads with "
        f"{format_currency(best_country_row['Revenue'])} in total revenue."
    )

    st.info(
        f"**Top product:** \"{best_product_row['Description']}\" is the highest "
        f"revenue-generating product, at {format_currency(best_product_row['Revenue'])}."
    )

with obs2:

    st.info(
        f"**Busiest day:** {best_day_row['DayName']} sees the highest average "
        f"revenue across the week."
    )

    st.info(
        f"**Weekend share:** Weekend purchases account for "
        f"{weekend_share:.1f}% of total revenue."
    )

    st.info(
        f"**Average order value:** Each transaction is worth "
        f"{format_currency(avg_order_value)} on average."
    )

st.divider()

# ==========================================================
# NAVIGATION
# ==========================================================

nav_left, nav_right = st.columns(2)

with nav_left:

    st.caption("⬅ Previous Page: Home")

with nav_right:

    st.caption("➡ Next Page: Customer Segmentation")
