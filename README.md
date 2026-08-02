# 📊 Intelligent Customer Analytics Platform

An end-to-end Machine Learning platform built on the **Online Retail dataset**, combining customer segmentation, predictive modelling, and a recommendation engine into a single interactive business intelligence dashboard.

The platform takes raw e-commerce transaction data all the way through cleaning, exploratory analysis, feature engineering, model training, and prediction — and presents the results through a multi-page **Streamlit** dashboard designed for both technical and non-technical stakeholders.

---

## 🧭 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Dataset](#-dataset)
- [Machine Learning Pipeline](#-machine-learning-pipeline)
- [Models Used](#-models-used)
- [Dashboard Pages](#-dashboard-pages)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Running the Dashboard](#-running-the-dashboard)
- [Business Problems Solved](#-business-problems-solved)
- [Project Highlights](#-project-highlights)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🎯 Overview

Most portfolio projects stop at a single model in a notebook. This project instead simulates a **real-world retail analytics solution**: multiple ML models, a recommendation system, and an executive dashboard, all built on one dataset and wired together into one application.

The complete workflow goes:

```
Raw Transaction Data
      │
      ▼
Data Cleaning & Validation
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering (RFM)
      │
      ▼
   ┌──┴───────────────┬──────────────────┬────────────────────┐
   ▼                  ▼                  ▼                    ▼
Customer          CLV               Churn              Recommendation
Segmentation    Prediction        Prediction              System
   │                  │                  │                    │
   └──────────────────┴──────────────────┴────────────────────┘
                              │
                              ▼
                 Interactive Streamlit Dashboard
```

---

## ✨ Key Features

**Analytics**
- Executive KPIs and revenue trend analysis
- Country, product, and time-based sales breakdowns
- Interactive filters and CSV export on every page

**Machine Learning**
- Customer segmentation via K-Means clustering on RFM features
- Customer Lifetime Value (CLV) prediction via regression
- Churn prediction via classification
- Three recommendation engines: popularity ranking, customer collaborative filtering, and item-item similarity — plus a hybrid blend of the last two

**Business Applications**
- Segment-specific retention and growth strategies
- Risk-tiered churn playbooks
- Product cross-sell and upsell recommendations
- Executive-level business health summary (revenue concentration risk, top performers)

---

## 📂 Dataset

The **Online Retail dataset** contains real transactional records from a UK-based online retailer.

| Attribute     | Value            |
|---------------|-------------------|
| Domain        | E-Commerce        |
| Customers     | 5,900+            |
| Transactions  | 500,000+          |
| Products      | 4,000+            |
| Countries     | 38                |

**Raw fields:** Invoice Number, Stock Code, Product Description, Quantity, Invoice Date, Unit Price, Customer ID, Country.

From this raw data, the pipeline derives cleaned transaction records (`final_cleaned_dataset.csv`), per-customer RFM features (`customer_features.csv`), and the model-ready datasets used throughout the dashboard.

---

## 🔬 Machine Learning Pipeline

| Phase | Description |
|-------|-------------|
| 1. Business Understanding | Defined the core questions: who are our customers, which are valuable, which are at risk, and what should they buy next. |
| 2. Data Cleaning | Removed cancelled orders, invalid customer IDs, negative quantities, and duplicate records. |
| 3. Exploratory Data Analysis | Explored revenue trends, top products, top countries, and time-based purchase patterns. |
| 4. Feature Engineering | Built Recency, Frequency, and Monetary (RFM) features per customer, plus average revenue and unique products purchased. |
| 5. Customer Segmentation | Applied K-Means clustering on RFM features to group customers into behavioural segments. |
| 6. CLV Prediction | Trained a regression model to predict each customer's future lifetime value. |
| 7. Churn Prediction | Trained a classification model to estimate each customer's probability of churning. |
| 8. Recommendation System | Built three recommendation engines: popularity, collaborative filtering, and item similarity. |
| 9. Dashboard Development | Brought every model and dataset together into the Streamlit dashboard. |

---

## 🧠 Models Used

| Task | Approach |
|------|----------|
| Customer Segmentation | K-Means Clustering |
| CLV Prediction | Regression |
| Churn Prediction | Classification |
| Recommendation (Popularity) | Ranking by purchase volume & revenue |
| Recommendation (Collaborative) | Nearest-neighbour collaborative filtering |
| Recommendation (Item Similarity) | Item-item similarity |

---

## 🖥 Dashboard Pages

| Page | What It Shows |
|------|----------------|
| **Home** | Project introduction, completed phases, platform architecture |
| **Data Overview** | Dataset KPIs, revenue/quantity trends, top countries & products, time-based patterns, interactive filters |
| **Customer Segmentation** | Segment distribution, RFM comparison across segments, customer value map, segment leaderboard, business recommendations per segment |
| **CLV Prediction** | Actual vs. predicted CLV, value categories (High/Medium/Low), top customers, a quick CLV estimator |
| **Churn Prediction** | Churn risk categories, probability distribution, top at-risk customers, a quick churn estimator, retention playbook |
| **Recommendation System** | Most popular products, customer-specific recommendations, product similarity explorer, hybrid recommendation preview |
| **Business Insights** | Executive KPIs, revenue by segment/country/product, business health summary, strategic recommendations |
| **About** | Project objectives, pipeline, tech stack, and project structure |

Every chart and table on every page is computed live from the project's own processed data — nothing is hardcoded or pulled from an external source.

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Data Processing | NumPy, Pandas |
| Visualization | Plotly |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| Backend (planned) | FastAPI |
| Deployment (planned) | Docker |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```
Intelligent-Customer-Analytics-Platform/
│
├── data/
│   ├── raw/                       # Original, untouched dataset
│   ├── processed/                 # Cleaned data, features, segments, predictions
│   └── recommendation/            # Popularity, collaborative & item-similarity outputs
│
├── models/
│   ├── clv_model.pkl              # Trained CLV regression model
│   ├── clv_scaler.pkl
│   ├── churn_model.pkl            # Trained churn classification model
│   └── churn_scaler.pkl
│
├── assets/
│   ├── logo.png
│   ├── banner.png
│   ├── workflow.png
│   └── project_architecture.png
│
├── reports/
│   └── figures/                   # Exported charts and analysis reports
│
├── dashboard/
│   ├── app.py                     # Streamlit entry point
│   ├── pages/                     # One file per dashboard page
│   │   ├── 1_Home.py
│   │   ├── 2_Data_Overview.py
│   │   ├── 3_Customer_Segmentation.py
│   │   ├── 4_CLV_Prediction.py
│   │   ├── 5_Churn_Prediction.py
│   │   ├── 6_Recommendation_System.py
│   │   ├── 7_Business_Insights.py
│   │   └── 8_About.py
│   ├── utils/
│   │   ├── config.py               # Central paths & app configuration
│   │   ├── cache.py                # Cached data/model loaders
│   │   ├── data_loader.py          # Dataset-specific loading functions
│   │   └── helper.py               # Formatting helpers (currency, numbers)
│   └── styles/
│       └── style.css               # Dashboard theme
│
└── README.md
```

---

## ⚙️ Installation

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

Core dependencies used across this project:

```
pandas
numpy
scikit-learn
streamlit
plotly
```

---

## ▶️ Running the Dashboard

From the project root:

```bash
streamlit run dashboard/app.py
```

The dashboard will open automatically in your browser, typically at:

```
http://localhost:8501
```

---

## 💼 Business Problems Solved

**Who are our best customers?**
Solved through customer segmentation and the CLV model, which rank customers by predicted long-term value.

**Who is about to leave?**
Solved through the churn prediction model, which flags customers by churn probability so retention efforts can be targeted where they matter most.

**What should we recommend?**
Solved through three recommendation engines — popularity, collaborative filtering, and item similarity — combined into a hybrid preview.

**Where is revenue coming from?**
Solved through the Data Overview and Business Insights pages, which break revenue down by country, product, and time.

---

## 🏆 Project Highlights

- ✔ Production-ready folder structure
- ✔ Modular, reusable pipeline code
- ✔ Multiple trained Machine Learning models (clustering, regression, classification)
- ✔ Hybrid recommendation engine combining two independent algorithms
- ✔ Interactive, multi-page Streamlit dashboard with 8 dedicated pages
- ✔ Executive-level business insights, computed live from the data
- ✔ Deployment-ready architecture (FastAPI + Docker)

---

## 🚀 Future Improvements

- Deploy the dashboard to the cloud
- Deploy the FastAPI backend as a live, queryable API
- Add real-time customer predictions instead of static CSV outputs
- Integrate a proper database instead of static CSVs
- Add an authentication layer for internal use
- Add model monitoring and drift detection
- Expose recommendations through a public API
- Automate report generation on a schedule

---

## 👨‍💻 Author

**Arin Bhardwaj**
M.Sc. Mathematics and Scientific Computing, NIT Warangal

**Project:** Intelligent Customer Analytics Platform
**Type:** End-to-End Machine Learning Project

---

*Built with Python, Scikit-learn, Streamlit, and Plotly.*