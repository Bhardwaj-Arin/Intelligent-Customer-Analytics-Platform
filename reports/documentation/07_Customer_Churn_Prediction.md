# Phase 7: Customer Churn Prediction

## Overview

The objective of this phase is to build a machine learning model capable of identifying customers who are likely to stop purchasing from the business.

Unlike Customer Lifetime Value (CLV) Prediction, which estimates future customer revenue, churn prediction focuses on identifying customers who are at risk of becoming inactive. Early identification of these customers allows businesses to implement targeted retention strategies, reduce revenue loss, and improve long-term customer relationships.

Since the Online Retail dataset does not contain an explicit churn label, a business-driven churn definition was created. Customers who had not made any purchases during the final 90 days of the observation period were labeled as churned.

This transformed the problem into a supervised binary classification task.

---

# Objectives

- Define a business-driven churn target.
- Create a customer-level churn dataset.
- Train multiple classification models.
- Compare model performance using multiple evaluation metrics.
- Identify the best-performing model.
- Generate churn predictions and churn probabilities.
- Save the trained model for deployment.
- Extract business insights from the results.

---

# Workflow

Raw Transaction Data

↓

Create Churn Target

↓

Merge Customer Features

↓

Prepare Modeling Dataset

↓

Train-Test Split

↓

Feature Scaling

↓

Train Classification Models

↓

Evaluate Models

↓

Compare Performance

↓

Feature Importance Analysis

↓

Generate Customer Predictions

↓

Save Final Model

↓

Business Insights

---

# Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier
- Extra Trees Classifier

---

# Evaluation Metrics

Model performance was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix
- ROC Curve

These metrics provide a comprehensive understanding of each model's classification performance.

---

# Outputs

## Datasets

- customer_churn_dataset.csv
- customer_churn_predictions.csv

## Models

- churn_model.pkl
- churn_scaler.pkl

## Figures

- churn_distribution.png
- churn_pie_chart.png
- churn_correlation_heatmap.png
- confusion_matrix.png
- roc_curve.png
- model_accuracy_comparison.png
- model_comparison_churn.png
- model_metrics_comparison.png
- feature_importance_churn.png
- cumulative_feature_importance.png

---

# Business Value

The churn prediction model enables businesses to:

- Identify customers who are likely to churn.
- Prioritize high-risk customers using churn probabilities.
- Improve customer retention campaigns.
- Optimize marketing budgets.
- Reduce revenue loss.
- Support data-driven decision-making.

---

# Conclusion

This phase successfully developed a complete customer churn prediction pipeline using supervised machine learning. Historical customer transaction data was transformed into actionable business insights through feature engineering, classification modeling, performance evaluation, and prediction generation.

The resulting model is deployment-ready and will be integrated into the Streamlit dashboard and FastAPI backend in the upcoming phases of the project.