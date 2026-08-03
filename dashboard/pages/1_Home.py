"""
Home Page
-------------------------------------------------------------

The landing page of the Intelligent Customer Analytics Platform.
Gives a quick executive snapshot of the dataset, the completed
project phases, and the platform's architecture.

Every number on this page is computed directly from the
project's own cleaned dataset via load_cleaned_data(). No
external data, images, or text is used anywhere on this page.

Author: Arin Bhardwaj
Project: Intelligent Customer Analytics Platform
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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

# ==========================================================
# BUSINESS METRICS
# ==========================================================

total_customers = df["CustomerID"].nunique()

total_transactions = df["InvoiceNo"].nunique()

total_products = df["StockCode"].nunique()

total_revenue = df["Revenue"].sum()

total_countries = df["Country"].nunique()

avg_order_value = (
    total_revenue / total_transactions if total_transactions > 0 else 0
)

# ==========================================================
# HERO SECTION
# ==========================================================

st.title("📊 Intelligent Customer Analytics Platform")

st.markdown(
    """
This platform was built to simulate a real-world retail analytics
solution used by modern organizations.

Instead of focusing on a single Machine Learning model, it
integrates multiple analytics modules into one centralized
dashboard — taking raw customer transaction data through
cleaning, feature engineering, predictive modelling, and
customer intelligence, all the way to an executive business
dashboard.

The objective: help business stakeholders understand customer
behaviour, predict future outcomes, identify valuable customers,
reduce churn, and recommend relevant products.
"""
)

st.divider()

# ==========================================================
# KPI OVERVIEW
# ==========================================================

st.header("📌 Platform at a Glance")

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "Customers",
        f"{total_customers:,}",
    )

with k2:

    st.metric(
        "Transactions",
        f"{total_transactions:,}",
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

k5, k6 = st.columns(2)

with k5:

    st.metric(
        "Total Revenue",
        format_currency(total_revenue),
    )

with k6:

    st.metric(
        "Avg Order Value",
        format_currency(avg_order_value),
    )

st.divider()

# ==========================================================
# PROJECT COMPLETION GAUGE
# ==========================================================

st.header("🎯 Project Completion")

total_phases = 9

completed_phases = 9

project_progress = round((completed_phases / total_phases) * 100)

fig_gauge = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=project_progress,
        number={"suffix": "%"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#3b82f6"},
            "steps": [
                {"range": [0, 50], "color": "#1e293b"},
                {"range": [50, 100], "color": "#334155"},
            ],
        },
    )
)

fig_gauge.update_layout(
    height=300,
    margin=dict(l=20, r=20, t=30, b=10),
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"),
)

st.plotly_chart(
    fig_gauge,
    use_container_width=True,
)

st.divider()

# ==========================================================
# COMPLETED PROJECT PHASES
# ==========================================================

st.header("📂 Completed Project Phases")

st.caption(
    "Every phase of this project has been completed following an "
    "industry-standard Machine Learning workflow."
)

phase_names = [
    "Business Understanding",
    "Data Cleaning Pipeline",
    "Exploratory Data Analysis",
    "Feature Engineering",
    "Customer Segmentation",
    "Customer Lifetime Value Prediction",
    "Customer Churn Prediction",
    "Recommendation System",
    "Interactive Streamlit Dashboard",
]

phase_columns = st.columns(3)

for index, phase_name in enumerate(phase_names):

    with phase_columns[index % 3]:

        st.success(f"✅ Phase {index + 1}\n\n**{phase_name}**")

st.divider()

# ==========================================================
# END-TO-END WORKFLOW
# ==========================================================

st.header("⚙️ End-to-End Machine Learning Workflow")

st.caption(
    "The project follows a complete industry-standard Data Science "
    "lifecycle, from raw transactional data to intelligent business "
    "recommendations."
)

workflow_df = pd.DataFrame(
    {
        "Stage": [
            "Business Understanding",
            "Data Cleaning",
            "EDA",
            "Feature Engineering",
            "Segmentation",
            "CLV",
            "Churn",
            "Recommendation",
            "Dashboard",
        ],
        "Completion": [100] * 9,
    }
)

fig_workflow = px.bar(
    workflow_df,
    x="Completion",
    y="Stage",
    orientation="h",
    template="plotly_dark",
)

fig_workflow.update_layout(
    height=420,
    yaxis=dict(autorange="reversed"),
    xaxis=dict(range=[0, 100]),
    margin=dict(l=10, r=10, t=10, b=10),
    showlegend=False,
)

st.plotly_chart(
    fig_workflow,
    use_container_width=True,
)

st.divider()

# ==========================================================
# PLATFORM ARCHITECTURE
# ==========================================================

st.header("🏗 Platform Architecture")

st.caption(
    "The complete solution consists of multiple integrated analytics "
    "modules working together."
)

arch_col1, arch_col2, arch_col3, arch_col4 = st.columns(4)

with arch_col1:

    st.info(
        """
**📁 Data Layer**

- Raw dataset
- Validation
- Cleaning
- Transformation
"""
    )

with arch_col2:

    st.info(
        """
**⚙️ Processing Layer**

- Feature engineering
- RFM analysis
- Encoding
- Scaling
"""
    )

with arch_col3:

    st.info(
        """
**🤖 ML Layer**

- Segmentation
- CLV prediction
- Churn prediction
- Recommendation
"""
    )

with arch_col4:

    st.info(
        """
**📊 Presentation Layer**

- Streamlit
- Interactive dashboard
- Business insights
- Decision support
"""
    )

st.divider()

# ==========================================================
# CORE PLATFORM FEATURES
# ==========================================================

st.header("⭐ Core Platform Features")

feature_col1, feature_col2, feature_col3 = st.columns(3)

with feature_col1:

    st.subheader("📊 Analytics")

    st.markdown(
        """
- Executive KPIs
- Revenue analytics
- Customer behaviour
- Country performance
- Product insights
- Interactive dashboard
"""
    )

with feature_col2:

    st.subheader("🤖 Machine Learning")

    st.markdown(
        """
- Customer segmentation
- CLV prediction
- Churn prediction
- Recommendation engine
- Model evaluation
- Business intelligence
"""
    )

with feature_col3:

    st.subheader("💼 Business Applications")

    st.markdown(
        """
- Customer retention
- Marketing strategy
- Revenue optimization
- Product recommendation
- Executive reporting
- Decision support
"""
    )

st.divider()

# ==========================================================
# TOP COUNTRIES BY REVENUE
# ==========================================================

st.header("🌍 Top Countries by Revenue")

st.caption("Countries generating the highest revenue.")

top_countries = (
    df.groupby("Country", as_index=False)["Revenue"]
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
    height=420,
    yaxis=dict(autorange="reversed"),
    margin=dict(l=10, r=10, t=10, b=10),
)

st.plotly_chart(
    fig_top_countries,
    use_container_width=True,
)

top_country_row = top_countries.iloc[0]

st.success(
    f"💡 **Business Recommendation:** Focus customer retention campaigns "
    f"in {top_country_row['Country']} and other high-revenue markets, "
    f"while identifying opportunities in lower-performing regions."
)

st.divider()

# ==========================================================
# BEST SELLING PRODUCTS
# ==========================================================

st.header("📦 Best Selling Products")

st.caption("Products contributing the highest sales volume.")

top_products = (
    df.groupby("Description", as_index=False)["Quantity"]
    .sum()
    .sort_values("Quantity", ascending=False)
    .head(10)
)

fig_top_products = px.bar(
    top_products,
    x="Quantity",
    y="Description",
    orientation="h",
    template="plotly_dark",
)

fig_top_products.update_layout(
    height=420,
    yaxis=dict(autorange="reversed"),
    margin=dict(l=10, r=10, t=10, b=10),
)

st.plotly_chart(
    fig_top_products,
    use_container_width=True,
)

st.divider()

# ==========================================================
# NAVIGATION
# ==========================================================

st.header("🧭 Explore the Platform")

nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

with nav_col1:

    st.page_link("pages/2_Data_Overview.py", label="📊 Data Overview")

    st.page_link("pages/3_Customer_Segmentation.py", label="👥 Customer Segmentation")

with nav_col2:

    st.page_link("pages/4_CLV_Prediction.py", label="💰 CLV Prediction")

    st.page_link("pages/5_Churn_Prediction.py", label="⚠️ Churn Prediction")

with nav_col3:

    st.page_link("pages/6_Recommendation_System.py", label="🎯 Recommendation System")

    st.page_link("pages/7_Business_Insights.py", label="📈 Business Insights")

with nav_col4:

    st.page_link("pages/8_About.py", label="ℹ️ About")

st.divider()

st.caption("Intelligent Customer Analytics Platform · Built with Streamlit & Plotly")
