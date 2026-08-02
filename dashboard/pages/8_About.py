"""
About Page
-------------------------------------------------------------

This page describes the Intelligent Customer Analytics Platform
itself: what it does, how it was built, the pipeline it follows,
and the technology behind it.

Unlike the other pages, this page does not load a dataset — it
documents the project. Every fact here (module names, phases,
tech stack, dataset scale) describes this project's own pipeline
and codebase. No external project, company, or template content
is used anywhere on this page.

Author: Arin Bhardwaj
Project: Intelligent Customer Analytics Platform
"""

import pandas as pd
import streamlit as st

# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("ℹ️ About This Platform")

st.markdown(
    """
The **Intelligent Customer Analytics Platform** is an end-to-end
Machine Learning solution built on the Online Retail dataset.

It combines customer segmentation, predictive modelling, and a
recommendation engine into a single interactive business
intelligence dashboard — taking raw transaction data all the way
through to executive-ready insights.
"""
)

st.divider()

# ==========================================================
# PROJECT OBJECTIVES
# ==========================================================

st.header("🎯 Project Objectives")

objective_left, objective_right = st.columns(2)

with objective_left:

    st.markdown(
        """
- Understand customer purchasing behaviour
- Segment customers using unsupervised learning
- Predict Customer Lifetime Value (CLV)
- Predict customer churn risk
"""
    )

with objective_right:

    st.markdown(
        """
- Recommend relevant products to customers
- Summarize findings into business insights
- Present everything through an interactive dashboard
- Structure the project for deployment (FastAPI + Docker)
"""
    )

st.divider()

# ==========================================================
# WHAT THIS DASHBOARD DOES
# ==========================================================

st.header("🧭 What This Dashboard Does")

feature_left, feature_mid, feature_right = st.columns(3)

with feature_left:

    st.subheader("📊 Understand")

    st.write(
        "Explore the raw dataset — sales trends, top products, top "
        "markets, and customer behaviour over time."
    )

with feature_mid:

    st.subheader("🤖 Predict")

    st.write(
        "Segment customers, predict lifetime value, and flag churn "
        "risk using models trained on this project's own data."
    )

with feature_right:

    st.subheader("💡 Recommend")

    st.write(
        "Suggest relevant products to customers using popularity "
        "ranking, collaborative filtering, and item similarity."
    )

st.divider()

# ==========================================================
# PROJECT PHASES
# ==========================================================

st.header("📌 Project Phases")

st.caption(
    "Every phase of this project, from raw data to a working dashboard."
)

phases = pd.DataFrame(
    {
        "Phase": [f"Phase {i}" for i in range(1, 10)],
        "Name": [
            "Business Understanding",
            "Data Cleaning",
            "Exploratory Data Analysis",
            "Feature Engineering",
            "Customer Segmentation",
            "CLV Prediction",
            "Churn Prediction",
            "Recommendation System",
            "Dashboard Development",
        ],
        "Status": ["✅ Completed"] * 9,
    }
)

st.dataframe(
    phases,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# MACHINE LEARNING PIPELINE
# ==========================================================

st.header("🤖 Machine Learning Pipeline")

st.caption(
    "The full pipeline this project follows, from raw data to a "
    "customer-facing dashboard."
)

pipeline_steps = [
    (
        "1. Business Understanding",
        "Defined the business questions: who are our customers, which "
        "ones are valuable, which are at risk, and what should they "
        "buy next.",
    ),
    (
        "2. Data Cleaning",
        "Removed cancelled orders, invalid customer IDs, negative "
        "quantities, and duplicate records from the raw Online Retail "
        "transaction data.",
    ),
    (
        "3. Exploratory Data Analysis",
        "Explored revenue trends, top products, top countries, and "
        "time-based purchase patterns to understand the shape of the "
        "data before modelling.",
    ),
    (
        "4. Feature Engineering",
        "Built Recency, Frequency, and Monetary (RFM) features per "
        "customer, along with average revenue and unique products "
        "purchased.",
    ),
    (
        "5. Customer Segmentation",
        "Applied K-Means clustering on RFM features to group customers "
        "into behavioural segments.",
    ),
    (
        "6. CLV Prediction",
        "Trained a regression model on customer features to predict "
        "each customer's future lifetime value.",
    ),
    (
        "7. Churn Prediction",
        "Trained a classification model to estimate each customer's "
        "probability of churning.",
    ),
    (
        "8. Recommendation System",
        "Built three recommendation engines: popularity ranking, "
        "customer collaborative filtering, and item-item similarity.",
    ),
    (
        "9. Dashboard Development",
        "Brought every model and dataset together into this "
        "interactive Streamlit dashboard.",
    ),
]

for step_title, step_description in pipeline_steps:

    with st.container(border=True):

        st.subheader(step_title)

        st.write(step_description)

st.divider()

# ==========================================================
# MODELS USED
# ==========================================================

st.header("🧠 Models Used")

models = pd.DataFrame(
    {
        "Task": [
            "Customer Segmentation",
            "CLV Prediction",
            "Churn Prediction",
            "Recommendation (Popularity)",
            "Recommendation (Collaborative)",
            "Recommendation (Item Similarity)",
        ],
        "Approach": [
            "K-Means Clustering",
            "Regression",
            "Classification",
            "Ranking by purchase volume & revenue",
            "Nearest-neighbour collaborative filtering",
            "Item-item similarity",
        ],
    }
)

st.dataframe(
    models,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# DATASET INFORMATION
# ==========================================================

st.header("📂 Dataset")

st.write(
    "The **Online Retail dataset** contains real transactional records "
    "from a UK-based online retailer, covering invoices, products, "
    "quantities, prices, customer IDs, and countries — the foundation "
    "for every module in this dashboard."
)

dataset_left, dataset_right = st.columns(2)

with dataset_left:

    st.subheader("Dataset Scale")

    dataset_info = pd.DataFrame(
        {
            "Attribute": [
                "Domain",
                "Customers",
                "Transactions",
                "Products",
                "Countries",
            ],
            "Value": [
                "E-Commerce",
                "5,900+",
                "500,000+",
                "4,000+",
                "38",
            ],
        }
    )

    st.dataframe(
        dataset_info,
        use_container_width=True,
        hide_index=True,
    )

with dataset_right:

    st.subheader("Raw Dataset Fields")

    raw_fields = [
        "Invoice Number",
        "Stock Code",
        "Product Description",
        "Quantity",
        "Invoice Date",
        "Unit Price",
        "Customer ID",
        "Country",
    ]

    for field in raw_fields:

        st.write(f"• {field}")

st.divider()

# ==========================================================
# BUSINESS PROBLEMS SOLVED
# ==========================================================

st.header("💼 Business Problems Solved")

problem_left, problem_right = st.columns(2)

with problem_left:

    st.info(
        """
**Who are our best customers?**

Solved through customer segmentation and the CLV model, which
rank customers by predicted long-term value.
"""
    )

    st.info(
        """
**Who is about to leave?**

Solved through the churn prediction model, which flags customers
by churn probability so retention efforts can be targeted.
"""
    )

with problem_right:

    st.info(
        """
**What should we recommend?**

Solved through three recommendation engines — popularity,
collaborative filtering, and item similarity — combined into a
hybrid preview.
"""
    )

    st.info(
        """
**Where is revenue coming from?**

Solved through the Data Overview and Business Insights pages,
which break revenue down by country, product, and time.
"""
    )

st.divider()

# ==========================================================
# PROJECT OUTPUTS
# ==========================================================

st.header("📊 Project Outputs")

outputs = pd.DataFrame(
    {
        "Output": [
            "Customer Segments",
            "CLV Predictions",
            "Churn Predictions",
            "Product Recommendations",
            "Business Insights",
            "Interactive Dashboard",
        ],
        "Where to Find It": [
            "Customer Segmentation page",
            "CLV Prediction page",
            "Churn Prediction page",
            "Recommendation System page",
            "Business Insights page",
            "This entire application",
        ],
    }
)

st.dataframe(
    outputs,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# PROJECT STRUCTURE
# ==========================================================

st.header("📁 Project Structure")

structure = pd.DataFrame(
    {
        "Folder": [
            "data/",
            "dashboard/",
            "models/",
            "notebooks/",
            "reports/",
            "src/",
        ],
        "Purpose": [
            "Raw and processed datasets used across the project",
            "This Streamlit application — pages, utils, and styles",
            "Trained model artifacts (segmentation, CLV, churn)",
            "Exploratory analysis and model development notebooks",
            "Generated reports and exported summaries",
            "Shared source code and pipeline scripts",
        ],
    }
)

st.dataframe(
    structure,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# TECHNOLOGY STACK
# ==========================================================

st.header("🛠 Technology Stack")

tech_stack = pd.DataFrame(
    {
        "Category": [
            "Programming Language",
            "Data Processing",
            "Visualization",
            "Machine Learning",
            "Dashboard",
            "Backend",
            "Deployment",
            "Version Control",
        ],
        "Technology": [
            "Python",
            "NumPy, Pandas",
            "Plotly",
            "Scikit-learn",
            "Streamlit",
            "FastAPI",
            "Docker",
            "Git & GitHub",
        ],
    }
)

st.dataframe(
    tech_stack,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# WHY EACH TOOL WAS CHOSEN
# ==========================================================

st.header("🔧 Why Each Tool Was Chosen")

tool_left, tool_right = st.columns(2)

with tool_left:

    st.markdown(
        """
**Pandas & NumPy** — cleaning, transforming, and aggregating
half a million transaction rows efficiently.

**Scikit-learn** — training the K-Means segmentation model, the
CLV regression model, and the churn classification model.
"""
    )

with tool_right:

    st.markdown(
        """
**Plotly** — every chart in this dashboard, chosen for its
interactivity (hover, zoom, filter) directly inside Streamlit.

**Streamlit** — turning all of the above into a single,
navigable, multi-page web application without writing frontend code.
"""
    )

st.divider()

# ==========================================================
# PROJECT MODULES
# ==========================================================

st.header("📦 Project Modules")

modules = pd.DataFrame(
    {
        "Module": [
            "Data Cleaning",
            "Exploratory Data Analysis",
            "Feature Engineering",
            "Customer Segmentation",
            "CLV Prediction",
            "Churn Prediction",
            "Recommendation System",
            "Business Dashboard",
        ],
        "Status": ["✅ Completed"] * 8,
    }
)

st.dataframe(
    modules,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# PROJECT HIGHLIGHTS
# ==========================================================

st.header("🏆 Project Highlights")

highlight_left, highlight_right = st.columns(2)

with highlight_left:

    st.success(
        """
✔ Production-ready folder structure

✔ Modular, reusable pipeline code

✔ Multiple trained Machine Learning models

✔ Hybrid recommendation engine
"""
    )

with highlight_right:

    st.success(
        """
✔ Interactive, multi-page Streamlit dashboard

✔ Executive-level business insights

✔ Deployment-ready architecture (FastAPI + Docker)

✔ Resume-ready portfolio project
"""
    )

st.divider()

# ==========================================================
# FUTURE IMPROVEMENTS
# ==========================================================

st.header("🚀 Future Improvements")

future_left, future_right = st.columns(2)

with future_left:

    st.info("Deploy the dashboard to the cloud")

    st.info("Deploy the FastAPI backend as a live API")

    st.info("Add real-time customer predictions")

    st.info("Integrate a proper database instead of static CSVs")

with future_right:

    st.info("Add an authentication layer for internal use")

    st.info("Add model monitoring and drift detection")

    st.info("Expose recommendations through a public API")

    st.info("Automate report generation on a schedule")

st.divider()

# ==========================================================
# DEVELOPER
# ==========================================================

st.header("👨‍💻 Developer")

developer_info = pd.DataFrame(
    {
        "Detail": [
            "Project",
            "Type",
            "Language",
            "Dashboard",
            "Backend",
            "Deployment",
        ],
        "Value": [
            "Intelligent Customer Analytics Platform",
            "End-to-End Machine Learning Project",
            "Python",
            "Streamlit",
            "FastAPI",
            "Docker",
        ],
    }
)

st.dataframe(
    developer_info,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# THANK YOU
# ==========================================================

st.header("🙏 Thank You")

st.success(
    """
Thank you for exploring the Intelligent Customer Analytics Platform.

This project demonstrates the complete lifecycle of a real-world
Machine Learning solution — from business understanding and data
preparation, through predictive analytics and recommendation
systems, to an interactive dashboard and deployment-ready
architecture.
"""
)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.caption("Intelligent Customer Analytics Platform · Built with Streamlit & Plotly")