import base64
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from utils.data_loader import load_cleaned_data
from utils.helper import format_currency

# ==========================================================
# 1. PAGE CONFIGURATION
# ==========================================================
st.set_page_config(
    page_title="Home | Intelligent Customer Analytics Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================================
# 2. DATA LOADING & GLOBAL METRICS
# ==========================================================
@st.cache_data(show_spinner=False)
def load_home_data():
    data = load_cleaned_data()
    data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])
    return data

df = load_home_data()

TOTAL_CUSTOMERS = df["CustomerID"].nunique()
TOTAL_TRANSACTIONS = df["InvoiceNo"].nunique()
TOTAL_PRODUCTS = df["StockCode"].nunique()
TOTAL_COUNTRIES = df["Country"].nunique()
TOTAL_REVENUE = float(df["Revenue"].sum())
AVG_ORDER_VALUE = TOTAL_REVENUE / TOTAL_TRANSACTIONS if TOTAL_TRANSACTIONS > 0 else 0

TOTAL_PHASES = 9
COMPLETED_PHASES = 9
PROJECT_PROGRESS = 100
TOTAL_MODELS = 8
TOTAL_DASHBOARDS = 8

# ==========================================================
# 3. HERO BANNER & PROJECT STATUS
# ==========================================================
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%); padding: 30px; border-radius: 12px; margin-bottom: 25px; border: 1px solid #334155;">
        <span style="background-color: #0284C7; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; letter-spacing: 1px;">
            🚀 PROJECT COMPLETED • END-TO-END MACHINE LEARNING PLATFORM
        </span>
        <h1 style="color: #F8FAFC; margin-top: 15px; margin-bottom: 10px; font-size: 36px;">
            Intelligent Customer Analytics Platform
        </h1>
        <p style="color: #94A3B8; font-size: 16px; line-height: 1.6; max-width: 900px;">
            Transforming raw retail transaction data into actionable business intelligence, customer segmentation, CLV prediction, churn prediction, and AI-powered recommendation systems through a single unified analytics dashboard.
        </p>
        <div style="margin-top: 20px; color: #38BDF8; font-size: 14px; font-weight: 500;">
            ✔ 9 Project Phases Completed &nbsp;&nbsp;•&nbsp;&nbsp;
            ✔ Interactive Business Dashboard &nbsp;&nbsp;•&nbsp;&nbsp;
            ✔ 8 Machine Learning Models &nbsp;&nbsp;•&nbsp;&nbsp;
            ✔ End-to-End Retail Workflow
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

hero_left, hero_right = st.columns([1.8, 1])

with hero_left:
    st.markdown(
        """
        ### 📖 Executive Platform Summary
        The **Intelligent Customer Analytics Platform** was engineered to simulate a real-world enterprise retail solution.
        
        Instead of treating Machine Learning as isolated algorithms, this platform connects every stage of the Data Science lifecycle—from raw transaction ingestion, data validation, and feature engineering to predictive modeling, churn risk mitigation, product recommendation, and executive KPI reporting.
        """
    )

with hero_right:
    fig_gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=PROJECT_PROGRESS,
            number={"suffix": "%"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#38BDF8"},
                "steps": [
                    {"range": [0, 25], "color": "#0F172A"},
                    {"range": [25, 50], "color": "#1E293B"},
                    {"range": [50, 75], "color": "#334155"},
                    {"range": [75, 100], "color": "#0284C7"},
                ],
            },
            title={"text": "Project Completion Status"},
        )
    )

    fig_gauge.update_layout(
        height=220,
        margin=dict(l=10, r=10, t=30, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
    )
    st.plotly_chart(fig_gauge, use_container_width=True, key="home_hero_gauge_chart")

st.divider()

# ==========================================================
# 4. EXECUTIVE BUSINESS OVERVIEW METRICS
# ==========================================================
st.subheader("📊 Executive Business Overview")
st.markdown("A macro snapshot of the retail transaction dataset powering the intelligence platform.")

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

with kpi1:
    st.metric("Total Revenue", format_currency(TOTAL_REVENUE), delta="Cleaned Baseline")
with kpi2:
    st.metric("Total Orders", f"{TOTAL_TRANSACTIONS:,}")
with kpi3:
    st.metric("Unique Customers", f"{TOTAL_CUSTOMERS:,}")
with kpi4:
    st.metric("Avg Order Value", format_currency(AVG_ORDER_VALUE))
with kpi5:
    st.metric("Global Markets", f"{TOTAL_COUNTRIES} Countries")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# 5. COMPLETED PROJECT PHASES GRID
# ==========================================================
st.subheader("📂 Completed Project Lifecycle Phases")
st.markdown("Every phase of the project followed an industry-standard Machine Learning pipeline.")

p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    st.success("✅ **Phase 1**: Business Understanding")
    st.success("✅ **Phase 2**: Data Cleaning & Pipeline")
    st.success("✅ **Phase 3**: Exploratory Data Analysis")

with p_col2:
    st.success("✅ **Phase 4**: Feature Engineering & RFM")
    st.success("✅ **Phase 5**: Customer Segmentation")
    st.success("✅ **Phase 6**: CLV Regression Models")

with p_col3:
    st.success("✅ **Phase 7**: Churn Risk Prediction")
    st.success("✅ **Phase 8**: Product Recommendation Engine")
    st.success("✅ **Phase 9**: Interactive Streamlit Platform")

st.divider()

# ==========================================================
# 6. PLATFORM WORKFLOW FUNNEL
# ==========================================================
st.subheader("⚙️ End-to-End Machine Learning Workflow")
st.markdown("Visualization of the sequential Data Science lifecycle implemented in this platform.")

workflow_df = pd.DataFrame(
    {
        "Phase": [
            "1. Business Understanding",
            "2. Data Ingestion & Cleaning",
            "3. Exploratory Data Analysis",
            "4. Feature Engineering",
            "5. Customer Segmentation",
            "6. CLV Prediction",
            "7. Churn Risk Modeling",
            "8. Recommendation Engine",
            "9. Executive Dashboard",
        ],
        "Completion": [100] * 9,
    }
)

fig_funnel = go.Figure(
    go.Funnel(
        y=workflow_df["Phase"],
        x=workflow_df["Completion"],
        textinfo="value+label",
        marker=dict(
            color=[
                "#E0F2FE",
                "#BAE6FD",
                "#7DD3FC",
                "#38BDF8",
                "#0284C7",
                "#0369A1",
                "#075985",
                "#0C4A6E",
                "#0F172A",
            ]
        ),
    )
)

fig_funnel.update_layout(
    height=450,
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"),
)

st.plotly_chart(fig_funnel, use_container_width=True, key="home_workflow_funnel_chart")

st.divider()

# ==========================================================
# 7. CORE PLATFORM CAPABILITIES
# ==========================================================
st.subheader("⭐ Core Platform Modules")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div style="background-color: #1E293B; padding: 20px; border-radius: 10px; border: 1px solid #334155; height: 100%;">
            <h4 style="color: #38BDF8; margin-top:0;">📊 Analytics & BI</h4>
            <ul style="color: #94A3B8; font-size: 14px; padding-left: 18px;">
                <li><b>Executive KPIs:</b> Macro revenue, order volume, and unit statistics.</li>
                <li><b>Temporal Trends:</b> Revenue trajectory and monthly seasonality.</li>
                <li><b>Geographic Insights:</b> Top country performance breakdowns.</li>
                <li><b>Data Quality Audits:</b> Cleaning rules and missing value handling.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div style="background-color: #1E293B; padding: 20px; border-radius: 10px; border: 1px solid #334155; height: 100%;">
            <h4 style="color: #818CF8; margin-top:0;">🤖 Machine Learning</h4>
            <ul style="color: #94A3B8; font-size: 14px; padding-left: 18px;">
                <li><b>RFM Segmentation:</b> Behavioral grouping (Champions, At-Risk, etc.).</li>
                <li><b>CLV Regressors:</b> Predicting 12-month future revenue potential.</li>
                <li><b>Churn Classifiers:</b> Predicting customer attrition probabilities.</li>
                <li><b>Recommender Systems:</b> Item-to-item collaborative filtering.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div style="background-color: #1E293B; padding: 20px; border-radius: 10px; border: 1px solid #334155; height: 100%;">
            <h4 style="color: #34D399; margin-top:0;">💼 Business Applications</h4>
            <ul style="color: #94A3B8; font-size: 14px; padding-left: 18px;">
                <li><b>Targeted Retention:</b> Early intervention for high-risk accounts.</li>
                <li><b>Marketing Optimization:</b> Campaign ROI estimators per segment.</li>
                <li><b>Cross-Selling:</b> Automated product bundle recommendations.</li>
                <li><b>Executive Reporting:</b> Exportable CSV lists and interactive filters.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

# ==========================================================
# 8. MACRO BUSINESS SAMPLES & HIGHLIGHTS
# ==========================================================
st.subheader("🌍 Revenue by Region & Top Selling Products")

top_col1, top_col2 = st.columns(2)

with top_col1:
    top_countries = (
        df.groupby("Country")["Revenue"]
        .sum()
        .reset_index()
        .sort_values(by="Revenue", ascending=False)
        .head(8)
    )

    fig_country_home = px.bar(
        top_countries,
        x="Revenue",
        y="Country",
        orientation="h",
        title="Top 8 Revenue Contributing Countries",
        color="Revenue",
        color_continuous_scale="Blues",
    )
    fig_country_home.update_layout(
        height=360,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F8FAFC"),
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False,
    )
    st.plotly_chart(fig_country_home, use_container_width=True, key="home_top_countries_chart")

with top_col2:
    top_products = (
        df.groupby("Description")["Quantity"]
        .sum()
        .reset_index()
        .sort_values(by="Quantity", ascending=False)
        .head(8)
    )

    fig_products_home = px.bar(
        top_products,
        x="Quantity",
        y="Description",
        orientation="h",
        title="Top 8 Products by Volume Sold",
        color="Quantity",
        color_continuous_scale="Teal",
    )
    fig_products_home.update_layout(
        height=360,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#F8FAFC"),
        yaxis=dict(categoryorder="total ascending"),
        coloraxis_showscale=False,
    )
    st.plotly_chart(fig_products_home, use_container_width=True, key="home_top_products_chart")

st.divider()

# ==========================================================
# 9. FOOTER
# ==========================================================
f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("### 📂 Dataset")
    st.caption("Online Retail Dataset • United Kingdom Retail Store • Cleaned Transactional Data")

with f2:
    st.markdown("### 🛠️ Built With")
    st.caption("Python • Pandas • Scikit-Learn • Plotly • Streamlit")

with f3:
    st.markdown("### ✅ Current Status")
    st.caption("✔ 9 Phases Completed • Dashboard Ready • Deployment Ready")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; color: #64748B; font-size: 14px;">
        Intelligent Customer Analytics Platform • Home Module
    </div>
    """,
    unsafe_allow_html=True,
)