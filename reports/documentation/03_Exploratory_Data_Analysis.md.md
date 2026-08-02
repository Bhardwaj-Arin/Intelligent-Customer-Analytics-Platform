# Phase 3: Exploratory Data Analysis (EDA)

## Overview

Exploratory Data Analysis (EDA) is one of the most important phases in any Data Science or Machine Learning project. Before building predictive models, it is essential to understand the dataset, identify hidden patterns, detect anomalies, validate data quality, and generate meaningful business insights.

In this phase, the cleaned retail transaction dataset was analyzed from multiple perspectives, including customer behavior, product performance, sales trends, geographic distribution, and customer segmentation. The objective was not only to understand the data but also to extract actionable insights that can support business decision-making.

This phase serves as the foundation for the Feature Engineering and Machine Learning phases.

---

# Objectives

The primary objectives of this phase were:

- Understand the overall distribution of the data.
- Analyze customer purchasing behavior.
- Identify sales trends over time.
- Discover high-value customers.
- Analyze product performance.
- Study country-wise business performance.
- Segment customers using the RFM framework.
- Identify relationships between important numerical variables.
- Generate business recommendations based on analytical findings.

---

# Workflow

The Exploratory Data Analysis was performed in the following sequence:

```
Dataset Overview
        ↓
Missing Value Analysis
        ↓
Duplicate Analysis
        ↓
Univariate Analysis
        ↓
Country Analysis
        ↓
Customer Analysis
        ↓
Time Series Analysis
        ↓
Customer Segmentation (RFM)
        ↓
Correlation Analysis
        ↓
Business Insights & Recommendations
```

---

# 1. Dataset Overview

## Objective

The first step was to understand the structure of the dataset.

The following information was examined:

- Dataset shape
- Column names
- Data types
- Statistical summary
- Missing values
- Duplicate values

## Why was this performed?

Before any analysis, it is important to understand what information is available and whether the dataset is suitable for analysis.

This step helps identify:

- Incorrect data types
- Missing values
- Potential data quality issues
- Numerical and categorical features

## Outcome

A clear understanding of the dataset structure and available features was obtained before beginning detailed analysis.

---

# 2. Missing Value Analysis

## Objective

Identify missing values within the dataset.

## Why was this performed?

Missing values can introduce bias and reduce model performance.

Understanding missing data helps determine whether records should be removed, imputed, or left unchanged.

## Outcome

- Missing Customer IDs were identified.
- Appropriate preprocessing had already been completed during the Data Cleaning phase.

---

# 3. Duplicate Analysis

## Objective

Detect duplicate records.

## Why was this performed?

Duplicate records can inflate sales, customer counts, and revenue calculations, leading to misleading insights.

## Outcome

Duplicate transactions had already been removed during preprocessing, ensuring reliable analysis.

---

# 4. Univariate Analysis

## Objective

Analyze each variable independently.

Variables analyzed included:

- Quantity
- Unit Price
- Revenue
- Country
- Cancellation Status

## Why was this performed?

Univariate analysis helps understand:

- Data distribution
- Range
- Skewness
- Outliers
- Central tendency

## Visualizations Used

- Histograms
- Boxplots
- Count plots

## Key Observations

- Revenue distribution was highly skewed.
- Most transactions involved relatively small purchase values.
- A small number of transactions contributed extremely high revenue.
- Several outliers represented genuine business activity rather than data errors.

---

# 5. Country Analysis

## Objective

Analyze business performance across different countries.

## Why was this performed?

Understanding geographic performance helps businesses identify strong markets and expansion opportunities.

## Analysis Performed

- Country-wise revenue
- Customer distribution by country

## Key Observations

- The United Kingdom generated the majority of revenue.
- International markets contributed additional revenue but at a smaller scale.
- Certain countries exhibited strong growth potential.

---

# 6. Customer Analysis

## Objective

Understand customer purchasing behavior.

## Analysis Performed

- Top customers by revenue
- Top customers by purchase frequency

## Why was this performed?

Businesses need to identify their most valuable customers for retention and personalized marketing strategies.

## Key Observations

- A relatively small group of customers generated a significant proportion of total revenue.
- Repeat customers contributed substantially more revenue than occasional buyers.
- High-value customers should be prioritized through loyalty programs.

---

# 7. Time Series Analysis

## Objective

Study sales performance over time.

## Analysis Performed

- Monthly revenue
- Monthly transactions
- Monthly active customers

## Why was this performed?

Time-series analysis identifies seasonal patterns and long-term business trends.

## Key Observations

- Revenue exhibited clear seasonal fluctuations.
- November consistently recorded the highest revenue.
- Customer activity increased during holiday shopping periods.
- Sales remained relatively stable throughout most of the year.

---

# 8. Customer Segmentation (RFM Analysis)

## Objective

Segment customers according to purchasing behavior.

RFM stands for:

- Recency
- Frequency
- Monetary Value

## Why was this performed?

Different customers require different marketing strategies.

RFM enables businesses to identify:

- Loyal customers
- High-value customers
- Lost customers
- At-risk customers

## Segments Created

- Champions
- Loyal Customers
- Potential Loyalists
- Big Spenders
- At Risk
- Lost Customers
- New Customers
- Others

## Key Observations

- Champions generated the highest revenue.
- Loyal Customers consistently contributed to business growth.
- Lost Customers showed high recency and low purchasing activity.
- Potential Loyalists represented an excellent opportunity for future growth.

---

# 9. Correlation Analysis

## Objective

Understand relationships between numerical variables.

## Analysis Performed

### Transaction-Level Correlation

Variables analyzed:

- Quantity
- Unit Price
- Revenue

### Customer-Level Correlation

Variables analyzed:

- Recency
- Frequency
- Monetary Value

## Why was this performed?

Correlation analysis helps identify variables that influence one another.

Understanding these relationships supports feature engineering and predictive modeling.

## Key Observations

- Frequency and Monetary Value showed a strong positive relationship.
- Customers who purchased more frequently generally spent more.
- Recency exhibited a negative relationship with Frequency and Monetary, indicating that inactive customers tend to spend less.

---

# 10. Business Insights

The analysis generated several important business insights.

## Customer Insights

- A small percentage of customers generated the majority of total revenue.
- Customer loyalty significantly influenced business revenue.
- High-value customers should receive personalized offers.

---

## Sales Insights

- Revenue increased during festive seasons.
- November represented the strongest sales month.
- Seasonal demand should guide inventory planning.

---

## Geographic Insights

- The United Kingdom remained the primary revenue source.
- International markets offer future growth opportunities.

---

## Product Insights

- High-demand products should receive inventory priority.
- Premium products generated substantial revenue despite lower sales volume.

---

# 11. Business Recommendations

Based on the analysis, the following recommendations were proposed:

- Reward Champions through loyalty programs.
- Re-engage Lost Customers using targeted marketing campaigns.
- Convert Potential Loyalists into Loyal Customers through personalized offers.
- Increase inventory before seasonal demand.
- Focus marketing on high-value customer segments.
- Expand successful products into international markets.
- Improve customer retention through personalized communication.

---

# Visualizations Generated

The following visualizations were created during this phase:

- Revenue Distribution
- Quantity Distribution
- Unit Price Distribution
- Country-wise Revenue
- Top Customers by Revenue
- Top Customers by Purchases
- Monthly Revenue Trend
- Monthly Transactions Trend
- Monthly Active Customers Trend
- Customer Segment Distribution
- Revenue Contribution by Segment
- Transaction Correlation Heatmap
- RFM Correlation Heatmap

These visualizations were saved in:

```
reports/figures/
```

for documentation, reporting, and future dashboard integration.

---

# Files Generated

During this phase, the following files were created:

```
notebooks/
└── 03_exploratory_data_analysis.ipynb

reports/
├── eda_report.md
└── figures/

data/processed/
├── final_cleaned_dataset.csv
└── customer_rfm.csv

docs/
└── 03_Exploratory_Data_Analysis.md
```

---

# Deliverables

At the end of this phase, the project produced:

- A fully analyzed retail dataset.
- Customer-level RFM dataset.
- Business insights and recommendations.
- Professional visualizations.
- Processed datasets for Machine Learning.
- Documentation for future reference.

---

# Conclusion

The Exploratory Data Analysis phase successfully transformed raw transactional data into meaningful business intelligence.

Through statistical analysis, visualization, customer segmentation, and trend analysis, valuable insights into customer behavior, purchasing patterns, and business performance were identified.

The outcomes of this phase provide a strong foundation for Feature Engineering, Machine Learning model development, and the creation of an interactive customer analytics dashboard.

With a comprehensive understanding of the data, the project is now ready to transition from **descriptive analytics** to **predictive analytics** in the next phase.