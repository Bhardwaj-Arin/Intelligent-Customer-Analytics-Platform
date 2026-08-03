# 🚀 Intelligent Customer Analytics Platform

<div align="center">

[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://intelligent-customer-analytics-platform-rjpaaejbalwimmv6xhvwen.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Pipeline-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-337AB7?style=for-the-badge)](https://xgboost.readthedocs.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Viz-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)

*An end-to-end Machine Learning & Business Intelligence platform that transforms raw e-commerce transaction data into customer segments, lifetime value forecasts, churn risk scores, and personalized product recommendations — all inside one interactive dashboard.*

[**Live Demo**](https://intelligent-customer-analytics-platform-rjpaaejbalwimmv6xhvwen.streamlit.app/) • [Overview](#-overview) • [Key Features](#-key-features) • [Methodology](#-methodology) • [Dashboard Pages](#-dashboard-pages) • [Getting Started](#️-getting-started)

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [System Architecture & Workflow](#-system-architecture--workflow)
- [Key Features](#-key-features)
- [Methodology](#-methodology)
  - [1. Data Cleaning & Validation](#1-data-cleaning--validation)
  - [2. Feature Engineering & RFM Modeling](#2-feature-engineering--rfm-modeling)
  - [3. Customer Segmentation (K-Means Clustering)](#3-customer-segmentation-k-means-clustering)
  - [4. Customer Lifetime Value (CLV) Prediction](#4-customer-lifetime-value-clv-prediction)
  - [5. Churn Prediction](#5-churn-prediction)
  - [6. Hybrid Recommendation System](#6-hybrid-recommendation-system)
- [Model Results](#-model-results)
- [Dataset](#-dataset)
- [Dashboard Pages](#-dashboard-pages)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#️-getting-started)
- [Business Impact](#-business-impact)
- [Known Limitations & Roadmap](#-known-limitations--roadmap)
- [Author](#-author)

---

## 🎯 Overview

Businesses collect enormous volumes of customer data but routinely struggle to turn it into decisions. Without proper analysis, it's hard to know who your best customers are, who's about to leave, or what to recommend to whom.

The **Intelligent Customer Analytics Platform** takes real transactional logs from the **Online Retail II dataset** — 797,815 cleaned transactions across 5,900+ customers, 4,000+ products, and 38 countries — and pushes them through a complete, reproducible pipeline covering four layers of analytics:

1. **Descriptive Analytics** — real-time sales KPIs, revenue trends, country and product performance, time-based purchase patterns.
2. **Behavioral Segmentation** — unsupervised customer grouping based on Recency, Frequency, and Monetary (RFM) value.
3. **Predictive Analytics** — forecasting Customer Lifetime Value (CLV) and estimating churn probability per customer.
4. **Prescriptive Systems** — personalized product recommendations via a hybrid of popularity ranking, collaborative filtering, and item-item similarity.

Unlike a project that ends inside a Jupyter notebook, every model here is wired into a live, 8-page **Streamlit dashboard** that a non-technical stakeholder can actually use.

**🔗 [Try the live app](https://intelligent-customer-analytics-platform-rjpaaejbalwimmv6xhvwen.streamlit.app/)**

---

## 🏗 System Architecture & Workflow

```
Raw Transaction Data (Online Retail II)
              │
              ▼
   Data Cleaning & Validation  ──────────►  final_cleaned_dataset.csv
              │                             (single canonical dataset)
              ▼
   Exploratory Data Analysis
              │
              ▼
   Feature Engineering (RFM)
              │
   ┌──────────┼────────────────┬─────────────────────┐
   ▼          ▼                ▼                      ▼
Customer    CLV              Churn              Recommendation
Segmentation Prediction     Prediction              System
(K-Means)  (Gradient        (Gradient          (Popularity + Item
            Boosting)        Boosting)           Similarity + CF)
   │          │                │                      │
   └──────────┴────────────────┴──────────────────────┘
                              │
                              ▼
              8-Page Interactive Streamlit Dashboard
                    (deployed on Streamlit Cloud)
```

Every stage is backed by version-controlled code in `src/`, a corresponding Jupyter notebook in `notebooks/`, and a written report in `reports/documentation/` — not just exploratory scratch work.

---

## ✨ Key Features

**Analytics**
- Executive KPIs and revenue trend analysis across 797K+ transactions
- Country, product, and time-based sales breakdowns (day-of-week, time-of-day, weekday vs. weekend)
- Interactive filters and CSV export on every dashboard page

**Machine Learning**
- Customer segmentation via K-Means clustering on RFM features
- Customer Lifetime Value prediction via a tuned Gradient Boosting regressor
- Churn prediction via a tuned Gradient Boosting classifier
- A hybrid recommendation engine combining popularity ranking, customer-based collaborative filtering, item-item similarity, and association rule mining

**Business Applications**
- Segment-specific retention and growth strategies
- Risk-tiered churn playbooks
- Product cross-sell and upsell recommendations
- Executive business health summary (revenue concentration risk, top performers)

---

## 🔬 Methodology

### 1. Data Cleaning & Validation

Raw transaction data is loaded, validated against an expected schema, and cleaned: duplicates removed, missing descriptions and customer IDs dropped, invalid (non-positive) prices filtered, and cancelled orders flagged. The pipeline then derives the full canonical schema in one pass — `Revenue`, and the time-based features `Year`, `Month`, `MonthName`, `Day`, `DayName`, `Hour`, `Quarter`, `DayOfWeek`, `Week`, `IsWeekend`, and `TimeOfDay` — producing a single reproducible dataset (`final_cleaned_dataset.csv`) that every later phase and every dashboard page reads from.

### 2. Feature Engineering & RFM Modeling

Per-customer features are built on top of the cleaned transactions: **Recency** (days since last purchase), **Frequency** (number of distinct orders), and **Monetary** (total spend), plus supporting features like average order revenue and unique products purchased. These RFM features are the foundation for every model downstream.

### 3. Customer Segmentation (K-Means Clustering)

Customers are grouped into **4 behavioral segments** using K-Means clustering on standardized RFM features, with cluster count selected via the elbow method and validated with silhouette analysis.

### 4. Customer Lifetime Value (CLV) Prediction

A regression model predicts each customer's future value from their RFM and purchase-behavior features. Several algorithms were benchmarked; **Gradient Boosting** was selected as the best-performing model.

### 5. Churn Prediction

A classification model estimates each customer's probability of churning based on recency, frequency, and engagement features. **Gradient Boosting** was again the top performer here, evaluated with a full confusion matrix and ROC curve.

### 6. Hybrid Recommendation System

Three independent recommendation strategies were built and evaluated side by side:

- **Popularity Ranking** — ranks products by purchase volume and revenue; works even for new customers with no history.
- **Customer Collaborative Filtering** — finds customers with similar purchase behavior and recommends what those "neighbors" bought.
- **Item-Item Similarity** — finds products frequently purchased together, supported by association rule mining.

The dashboard's Recommendation System page also blends similarity and popularity scores into a hybrid ranking for a given product.

---

## 📊 Model Results

| Model | Metric | Value |
|---|---|---|
| **Customer Segmentation** | Clusters | 4 |
| | Silhouette Score | 0.229 |
| **CLV Prediction** | Best Model | Gradient Boosting |
| | MAE | 173.17 |
| | RMSE | 479.67 |
| **Churn Prediction** | Best Model | Gradient Boosting |
| | Accuracy | 99.49% |
| | Precision / Recall / F1 | 0.9949 |
| | ROC-AUC | 0.9997 |

> **Note on CLV performance:** the current CLV regressor's R² is close to zero, meaning it isn't yet meaningfully outperforming a naive average-based prediction on held-out data. This is called out honestly here rather than hidden — see [Known Limitations](#-known-limitations--roadmap) for planned improvements. The churn model's near-perfect scores are also worth a second look before treating them as production-ready — extremely high classification metrics like this can sometimes indicate the model has (indirect) access to information that wouldn't be available at prediction time in a real deployment, so it's worth double-checking the feature set for that before relying on these numbers operationally.

Full metrics, confusion matrices, ROC curves, and feature importance charts are versioned in `artifacts/` and `reports/figures/`.

---

## 📂 Dataset

The **Online Retail II** dataset contains real transactional records from a UK-based online retailer.

| Attribute | Value |
|---|---|
| Domain | E-Commerce |
| Customers | 5,900+ |
| Cleaned Transactions | 797,815 |
| Products | 4,000+ |
| Countries | 38 |

**Raw fields:** Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer ID, Country.

**Canonical processed schema** (`data/processed/final_cleaned_dataset.csv`): `InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country, IsCancelled, Revenue, Year, Month, MonthName, Day, DayName, Hour, Quarter, DayOfWeek, Week, IsWeekend, TimeOfDay`.

---

## 🖥 Dashboard Pages

| Page | What It Shows |
|---|---|
| **Home** | Project introduction, completed phases, platform architecture |
| **Data Overview** | Dataset KPIs, revenue/quantity trends, top countries & products, time-based patterns |
| **Customer Segmentation** | Segment distribution, RFM comparison, customer value map, segment leaderboard, business recommendations per segment |
| **CLV Prediction** | Actual vs. predicted CLV, value categories (High/Medium/Low), top customers, a quick CLV estimator |
| **Churn Prediction** | Churn risk categories, probability distribution, top at-risk customers, retention playbook |
| **Recommendation System** | Most popular products, customer-specific recommendations, product similarity explorer, hybrid recommendation preview |
| **Business Insights** | Executive KPIs, revenue by segment/country/product, business health summary, strategic recommendations |
| **About** | Project objectives, pipeline, tech stack, and project structure |

Every chart and table is computed live from the project's own processed data.

---

## 🛠 Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.12 |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn, XGBoost, LightGBM |
| Visualization | Plotly, Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Utilities | SciPy, Joblib, OpenPyXL, Pillow |
| Deployment | Streamlit Community Cloud |

---

## 📁 Project Structure

```
Intelligent-Customer-Analytics-Platform/
│
├── config/
│   ├── config.py                  # Column names, thresholds, constants
│   └── paths.py                   # Centralized path definitions
│
├── data/
│   ├── processed/                 # final_cleaned_dataset.csv, features, segments, predictions
│   └── recommendation/            # Popularity, collaborative & item-similarity outputs
│
├── src/
│   ├── data/                      # loader.py, validator.py, cleaner.py, pipeline.py
│   ├── features/                  # churn_features.py
│   ├── models/                    # train_churn.py, predict_churn.py
│   ├── recommendation/            # popularity, collaborative, item-similarity, hybrid pipeline
│   └── utils/                     # model_utils.py
│
├── notebooks/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   ├── 05_Customer_Segmentation.ipynb
│   ├── 06_Customer_Lifetime_Value_Prediction.ipynb
│   ├── 07_customer_churn_prediction.ipynb
│   └── 08_Recommendation_System/  # Product analysis → hybrid pipeline, 6 notebooks
│
├── models/                        # clv_model.pkl, clv_scaler.pkl, churn_model.pkl, churn_scaler.pkl
│
├── artifacts/                     # Per-phase metrics: segmentation, clv, churn, recommendation
│
├── reports/
│   ├── documentation/             # Phase-by-phase written reports, business problem, data dictionary
│   └── figures/                   # 35+ exported charts (EDA, model evaluation, etc.)
│
├── dashboard/
│   ├── app.py                     # Streamlit entry point
│   ├── pages/                     # 1_Home.py ... 8_About.py
│   ├── components/                # charts, metrics, prediction, recommendation, sidebar
│   ├── utils/                     # config, cache, data_loader, artifact_loader, helper
│   └── styles/                    # style.css
│
├── tests/
├── requirements.txt
└── README.md
```

---

## ⚙️ Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/<your-username>/intelligent-customer-analytics-platform.git
cd intelligent-customer-analytics-platform
```

**2. Create a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. (Re)generate the canonical dataset from raw data, if needed**

```bash
jupyter notebook notebooks/02_Data_Cleaning.ipynb
```

Running the pipeline (`DataPipeline().run()`) produces `data/processed/final_cleaned_dataset.csv` — the single dataset every later notebook and every dashboard page reads from.

**5. Run the dashboard**

```bash
streamlit run dashboard/app.py
```

The dashboard opens at `http://localhost:8501`. Or skip all of this and just use the **[live deployed version](https://intelligent-customer-analytics-platform-rjpaaejbalwimmv6xhvwen.streamlit.app/)**.

---

## 💼 Business Impact

**Who are our best customers?**
Answered through customer segmentation and CLV prediction, which rank customers by predicted long-term value.

**Who is about to leave?**
Answered through the churn model, which flags customers by churn probability so retention effort goes where it matters.

**What should we recommend?**
Answered through three independent recommendation engines blended into a hybrid ranking.

**Where is revenue coming from?**
Answered through the Data Overview and Business Insights pages, breaking revenue down by country, product, and time.

---

## 🚧 Known Limitations & Roadmap

Being upfront about the current state of the models:

- **CLV regression** currently has an R² near zero on held-out data — it isn't yet clearly better than predicting the average CLV for everyone. Next steps: richer behavioral features, log-transforming the heavily skewed CLV target, and testing XGBoost/LightGBM against the current Gradient Boosting baseline.
- **Churn classification** metrics (99.5% accuracy, 0.9997 ROC-AUC) are unusually high and should be stress-tested — worth auditing the feature set for anything that could be leaking the target (e.g., a feature that's only knowable *after* churn has already happened) before treating this as production-ready.
- **Recommendation evaluation** artifacts exist (`artifacts/recommendation/evaluation_metrics.csv`) but aren't yet populated with headline numbers in this README — worth adding once formal offline evaluation (precision@k, recall@k) is finalized.

**Planned next steps:**
- Deploy a FastAPI backend for real-time predictions instead of static CSV outputs
- Add model monitoring and drift detection
- Add an authentication layer for internal use
- Automate report regeneration on a schedule
- Add a proper `LICENSE` file (not yet included in this repository)

---

## 👨‍💻 Author

**Arin Bhardwaj**
M.Sc. Mathematics and Scientific Computing, NIT Warangal

**Project:** Intelligent Customer Analytics Platform
**Live App:** [intelligent-customer-analytics-platform-rjpaaejbalwimmv6xhvwen.streamlit.app](https://intelligent-customer-analytics-platform-rjpaaejbalwimmv6xhvwen.streamlit.app/)

---

*Built with Python, Scikit-learn, XGBoost, Streamlit, and Plotly.*