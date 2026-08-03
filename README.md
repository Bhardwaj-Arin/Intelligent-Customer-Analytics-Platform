# 🚀 Intelligent Customer Analytics Platform

<div align="center">

[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://intelligent-customer-analytics-platform.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Pipeline-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Viz-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

*An end-to-end Machine Learning & Business Intelligence platform transforming raw e-commerce transaction data into actionable customer insights, predictive analytics, and personalized product recommendations.*

[Live Demo App](https://intelligent-customer-analytics-platform.streamlit.app) • [Overview](#-overview) • [Key Features](#-key-features) • [Theoretical Foundations](#-theoretical-foundations--methodology) • [Dashboard Pages](#-dashboard-pages) • [Getting Started](#%EF%B8%8F-getting-started)

</div>

---

## 📌 Table of Contents
- [Overview](#-overview)
- [System Architecture & Workflow](#-system-architecture--workflow)
- [Key Features](#-key-features)
- [Theoretical Foundations & Methodology](#-theoretical-foundations--methodology)
  - [1. Data Preprocessing & Validation](#1-data-preprocessing--validation)
  - [2. Feature Engineering & RFM Modeling](#2-feature-engineering--rfm-modeling)
  - [3. Customer Segmentation (K-Means Clustering)](#3-customer-segmentation-k-means-clustering)
  - [4. Customer Lifetime Value (CLV) Prediction](#4-customer-lifetime-value-clv-prediction)
  - [5. Churn Risk Analytics](#5-churn-risk-analytics)
  - [6. Hybrid Recommendation System](#6-hybrid-recommendation-system)
- [Dataset Characteristics](#-dataset-characteristics)
- [Dashboard Page Guide](#-dashboard-page-guide)
- [Tech Stack](#-tech-stack)
- [Project Directory Structure](#-project-directory-structure)
- [Getting Started](#%EF%B8%8F-getting-started)
- [Business Impact & Strategic Value](#-business-impact--strategic-value)
- [Roadmap & Future Enhancements](#-roadmap--future-enhancements)
- [Author](#-author)

---

## 🎯 Overview

Most portfolio machine learning projects terminate within isolated Jupyter Notebooks without providing an executive-facing interactive UI or real-world application. The **Intelligent Customer Analytics Platform** addresses this gap by creating an enterprise-grade analytics platform that converts raw e-commerce order logs into end-to-end data products.

Using real transactional logs from the **Online Retail II dataset** (containing over 500,000 transaction records), this platform cleans, engineers, models, and evaluates customer purchase behavior across multiple dimensions:

1. **Descriptive Analytics**: Real-time sales KPIs, temporal purchase distribution, geographical concentration, and high-volume product breakdown.
2. **Customer Behavioral Segmentation**: Unsupervised group discovery based on purchase recency, frequency, and monetary throughput.
3. **Predictive Analytics**: Forecasting future lifetime monetary yield (**CLV**) and quantifying customer departure probability (**Churn**).
4. **Prescriptive Systems**: Delivering personal product recommendations using a multi-algorithm hybrid approach (Popularity, Item-Item Similarity, Collaborative Filtering).

---

## 🏗 System Architecture & Workflow



┌─────────────────────────────────────────┐
                    │   Raw E-Commerce Transactional Data     │
                    │        (Online Retail II Dataset)       │
                    └────────────────────┬────────────────────┘
                                         │
                                         ▼
                    ┌─────────────────────────────────────────┐
                    │   Data Cleaning & Validation Pipeline   │
                    │ (Duplicates, Cancellations, Null IDs)   │
                    └────────────────────┬────────────────────┘
                                         │
                                         ▼
                    ┌─────────────────────────────────────────┐
                    │        RFM Feature Engineering          │
                    │    (Recency, Frequency, Monetary, etc)  │
                    └────────────────────┬────────────────────┘
                                         │
  ┌──────────────────────┬───────────────┴───────────────┬──────────────────────┐
  ▼                      ▼                               ▼                      ▼
┌───────────┐      ┌───────────────────┐           ┌───────────────────┐  ┌───────────────────┐
│ Customer  │      │   CLV Prediction  │           │  Churn Prediction │  │  Recommendation   │
│ Segments  │      │    (Regression)   │           │  (Classification) │  │  System (Hybrid)  │
└─────┬─────┘      └─────────┬─────────┘           └─────────┬─────────┘  └─────────┬─────────┘
│                      │                               │                      │
└──────────────────────┴───────────────┬───────────────┴──────────────────────┘
│
▼
┌─────────────────────────────────────────┐
│     Interactive Streamlit Dashboard     │
│         (8 Modular Page Views)          │
└─────────────────────────────────────────┘


---

## ✨ Key Features

- **Executive KPI Dashboard**: Live tracking of gross revenue, purchase frequencies, unit quantities, and top-performing markets.
- **Dynamic Data Filtering**: Interactive temporal, geographical, and SKU-level slice-and-dice tools on every page.
- **Automated Customer Segmentation**: Unsupervised RFM clustering with automated business persona labels (*Champions*, *Loyal*, *At Risk*, *Lost*).
- **Predictive CLV & Churn Estimators**: Interactive "What-If" scenarios allowing users to enter custom RFM parameters to compute live predictions.
- **3-Tiered Recommendation Engines**: Instant switching between baseline popularity models, item-item similarity matrices, user-collaborative filtering, and blended hybrid recommendations.
- **Executive Insight Generation**: Automated revenue concentration risk assessments, segment share distributions, and playbooks.

---

## 🔬 Theoretical Foundations & Methodology

### 1. Data Preprocessing & Validation
Raw e-commerce transaction data frequently suffers from formatting inconsistencies, system cancellations, and missing attribution.
- **Filtering Negative Values**: Quantities with negative values correspond to cancelled or returned orders (`InvoiceNo` starting with 'C'). These were removed to establish accurate net revenue values.
- **Missing Customer IDs**: Rows missing `CustomerID` cannot be attributed to specific historical accounts and are excluded from customer-level RFM modeling.
- **Price Anomaly Removal**: Transactions with zero or negative `UnitPrice` (e.g., administrative write-offs or system tests) were filtered out.

### 2. Feature Engineering & RFM Modeling
Customer behavior is summarized into a tabular feature set via the **Recency, Frequency, and Monetary (RFM)** framework:

$$\text{Recency (R)} = T_{\text{analysis}} - \max(T_{\text{customer\_purchase}})$$

$$\text{Frequency (F)} = \vert{}\{ \text{Unique Invoices per Customer} \}\vert{}$$

$$\text{Monetary (M)} = \sum (\text{Quantity} \times \text{UnitPrice})$$

Additional derived features include:
- **Average Order Value (AOV)**: $\frac{\text{Monetary}}{\text{Frequency}}$
- **Purchase Variety**: Count of unique product SKUs purchased (`StockCode`).

### 3. Customer Segmentation (K-Means Clustering)
- **Feature Scaling**: Due to the skewed nature of financial datasets, RFM metrics are log-transformed to normalize distributions and then scaled using `StandardScaler`:

  $$x' = \frac{\ln(x + 1) - \mu}{\sigma}$$

- **K-Means Optimization**: The optimal number of clusters ($k$) is evaluated using the **Elbow Method** (minimizing Within-Cluster Sum of Squares) and verified using the **Silhouette Coefficient**:

  $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$

  *where $a(i)$ is the mean intra-cluster distance and $b(i)$ is the mean nearest-cluster distance.*

### 4. Customer Lifetime Value (CLV) Prediction
Predicting future monetary spend over an extended horizon is framed as a supervised regression task.
- **Target Formulation**: Future monetary total over a target evaluation window.
- **Supervised Regression Pipeline**: Scaled behavioral inputs are trained using Scikit-Learn regression models (e.g., Linear Regression, Ridge, Random Forest) to output expected continuous values.
- **Evaluation Metrics**: Models are evaluated using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE):

  $$\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$

### 5. Churn Risk Analytics
A customer is classified as **Churned** if their inactivity period exceeds a specific recency threshold relative to standard purchase cycles.
- **Binary Target**: 
  $$\text{Churn} = \begin{cases} 1 & \text{if Recency} > \text{Threshold} \\ 0 & \text{otherwise} \end{cases}$$
- **Classification Modeling**: Probability outputs $P(\text{Churn}=1\vert{}\mathbf{X})$ are generated using supervised models (e.g., Logistic Regression, Gradient Boosting/Random Forests).
- **Risk Stratification**:
  - 🟢 **Low Risk**: $P(\text{Churn}) < 0.35$
  - 🟡 **Medium Risk**: $0.35 \le P(\text{Churn}) < 0.70$
  - 🔴 **High Risk**: $P(\text{Churn}) \ge 0.70$

### 6. Hybrid Recommendation System
The recommendation engine combines multiple recommendation approaches:
- **Popularity Engine**: Baseline top-seller ranking by order count and gross revenue.
- **Item-Item Cosine Similarity**: Measures similarity between product vector representations $u$ and $v$:

  $$\text{Cosine Similarity}(u, v) = \frac{u \cdot v}{\Vert{}u\Vert{}_2 \Vert{}v\Vert{}_2}$$

- **User-Based Collaborative Filtering**: Identifies $K$-nearest neighbor accounts with similar historical item choices.
- **Hybrid Blending**: Combines user preference scores and product similarity matrices to mitigate cold-start issues and maximize recommendation accuracy.

---

## 📊 Dataset Characteristics

The project uses the public **Online Retail II dataset** (UK-based e-commerce store).

| Attribute | Summary Specification |
| :--- | :--- |
| **Domain** | Non-store Online Retail / E-Commerce |
| **Total Order Records** | 500,000+ Records |
| **Active Customer Accounts** | 5,900+ Unique IDs |
| **Product Catalog** | 4,000+ Distinct SKUs |
| **Global Reach** | 38 Geographic Countries |
| **Raw Schema Attributes** | `Invoice`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `Price`, `Customer ID`, `Country` |

---

## 🖥 Dashboard Page Guide

| Page View | Content & Analytical Features | Primary Audience |
| :--- | :--- | :--- |
| **1. Home** | Architectural pipeline flow, project summary, tech badges, and repository guide | General / Evaluators |
| **2. Data Overview** | Interactive top-level KPIs, revenue trends over time, geographical maps, dynamic tables | Business Analysts |
| **3. Customer Segmentation** | RFM cluster distribution, 2D/3D scatter plots, profile centroids, and segment strategies | CRM & Marketing Teams |
| **4. CLV Prediction** | Predicted vs. actual CLV plots, value tiers (**High/Medium/Low**), interactive custom CLV calculator | Finance & Revenue Teams |
| **5. Churn Prediction** | Risk distribution charts, high-risk customer lookup tables, interactive churn estimator, retention guides | Customer Retention Teams |
| **6. Recommendation Engine** | Trending items list, customer collaborative recommendations, item-item similarity explorer | Product & Merchandising |
| **7. Business Insights** | Revenue concentration analytics, segment share breakdowns, strategic health metrics | C-Suite & Executives |
| **8. About** | Deep-dive methodology, system dependencies, model parameters, and contact links | Engineering & ML Leads |

---

## 🛠 Tech Stack

- **Programming Language**: Python 3.11+
- **Data Engineering**: Pandas, NumPy
- **Machine Learning & Modeling**: Scikit-Learn
- **Data Visualization**: Plotly, Matplotlib, Seaborn
- **Dashboard Web Framework**: Streamlit
- **Version Control & Repository**: Git, GitHub

---

## 📁 Project Directory Structure

```text
Intelligent-Customer-Analytics-Platform/
│
├── assets/                        # Diagrams, architectural flowcharts, UI icons
│   ├── banner.png
│   ├── logo.png
│   └── workflow.png
│
├── dashboard/                     # Multi-page Streamlit Application
│   ├── app.py                     # Primary Streamlit Entry Point
│   ├── pages/                     # Dedicated Sub-pages
│   │   ├── 1_Home.py
│   │   ├── 2_Data_Overview.py
│   │   ├── 3_Customer_Segmentation.py
│   │   ├── 4_CLV_Prediction.py
│   │   ├── 5_Churn_Prediction.py
│   │   ├── 6_Recommendation_System.py
│   │   ├── 7_Business_Insights.py
│   │   └── 8_About.py
│   ├── styles/                    # Visual Styling Assets
│   │   └── style.css               # Streamlit Theme Custom CSS
│   └── utils/                     # Data Loaders & Helper Scripts
│       ├── cache.py               # Streamlit Cache Optimizers
│       ├── config.py              # Path Definitions & System Settings
│       ├── data_loader.py         # CSV & Pipeline Loaders
│       └── helper.py              # Currency & Number Formatting Helpers
│
├── data/                          # Structured Data Storage
│   ├── raw/                       # Original Raw Transaction Dataset
│   ├── processed/                 # Cleaned Datasets & Feature Sets
│   └── recommendation/            # Precomputed Recommendation Matrices
│
├── models/                        # Serialized Model Artifacts
│   ├── churn_model.pkl            # Supervised Churn Classifier
│   ├── churn_scaler.pkl           # Churn Feature Scaler
│   ├── clv_model.pkl              # Supervised CLV Regressor
│   └── clv_scaler.pkl             # CLV Feature Scaler
│
├── reports/                       # Visual Artifact Exports
│   └── figures/                   # Exported Visual Analytics Plots
│
├── .gitignore
├── LICENSE                        # Open-Source License
├── README.md                      # Platform Documentation
└── requirements.txt               # System Dependencies