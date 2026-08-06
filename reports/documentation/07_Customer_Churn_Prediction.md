# Phase 7: Customer Churn Prediction

## Overview

The objective of this phase is to develop a robust machine learning pipeline capable of identifying customers who are at risk of discontinuing their purchases.

Customer churn prediction is one of the most valuable applications of predictive analytics because retaining existing customers is significantly more cost-effective than acquiring new ones. By identifying customers with a high probability of churning, businesses can implement proactive retention strategies, personalized marketing campaigns, loyalty programs, and targeted promotions to minimize revenue loss.

Since the Online Retail dataset does not contain an explicit churn label, a business-driven target variable was created. Customers whose **Recency** exceeded **90 days** were considered churned, transforming the problem into a supervised binary classification task.

This phase leverages the customer-level features engineered in Phase 4, including several advanced behavioural features such as purchase velocity, basket value, product diversity, purchase trend, and revenue trend, to build accurate churn prediction models.

Four machine learning algorithms were trained and evaluated. The best-performing model was selected based on multiple evaluation metrics and prepared for deployment within the Streamlit dashboard.

---

# Objectives

- Create a business-driven churn target variable.
- Build a customer-level churn prediction dataset.
- Train multiple supervised classification models.
- Compare model performance using multiple evaluation metrics.
- Select the best-performing model.
- Interpret model predictions using feature importance analysis.
- Validate feature importance using permutation importance.
- Serialize the final model and preprocessing artifacts for deployment.
- Generate actionable business insights for customer retention.

---

# Workflow

Customer Feature Dataset

↓

Create Churn Target Variable

↓

Feature Selection

↓

Train-Test Split

↓

Encode Categorical Features

↓

Feature Scaling

↓

Train Multiple Classification Models

↓

Evaluate Model Performance

↓

Compare All Models

↓

Feature Importance Analysis

↓

Permutation Feature Importance

↓

Model Serialization

↓

Business Insights

↓

Deployment Ready

---

# Machine Learning Models

The following classification algorithms were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

After comparing all models, **Random Forest Classifier** achieved the best overall performance and was selected as the final production model.

---

# Evaluation Metrics

Each model was evaluated using multiple performance metrics to ensure robust comparison:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Classification Report
- Confusion Matrix
- ROC Curve

These metrics provide a comprehensive evaluation of classification performance and class prediction quality.

---

# Model Performance Summary

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|---------:|----------:|--------:|---------:|---------:|
| Logistic Regression | **82.91%** | **82.89%** | **82.91%** | **82.89%** | **0.9214** |
| Decision Tree | **80.78%** | **80.76%** | **80.78%** | **80.77%** | **0.8079** |
| **Random Forest** | **85.37%** | **85.36%** | **85.37%** | **84.67%** | **0.9376** |
| XGBoost | **85.12%** | **85.10%** | **85.12%** | **84.51%** | **0.9400** |

**Best Model:** Random Forest Classifier

---

# Important Features

Feature importance analysis identified the following customer characteristics as the strongest predictors of churn:

- RevenueTrend
- PurchaseSpan
- PurchaseTrend
- TotalQuantity
- Monetary
- Frequency
- PurchaseVelocity
- UniqueProducts
- RevenueSTD
- AvgDaysBetweenPurchases

These features provide valuable business insights into customer purchasing behaviour and retention risk.

---

# Model Explainability

To improve model interpretability, **Permutation Feature Importance** was performed after model training.

Permutation importance evaluates each feature by measuring the decrease in model performance when that feature's values are randomly shuffled. Unlike built-in tree importance, this approach provides a model-agnostic estimate of feature relevance and helps validate which variables genuinely contribute to churn prediction.

The comparison between Random Forest Feature Importance and Permutation Feature Importance increases confidence in the reliability of the selected features.

---

# Outputs

## Datasets

- customer_features.csv (Updated with 31 engineered features)
- customer_churn_dataset.csv
- customer_churn_predictions.csv

---

## Saved Models

- customer_churn_random_forest.pkl
- customer_churn_scaler.pkl
- country_label_encoder.pkl
- feature_list.pkl
- model_information.pkl

---

## Figures

- churn_distribution.png
- confusion_matrix.png
- roc_curve.png
- model_comparison.png
- feature_importance.png
- cumulative_feature_importance.png
- permutation_feature_importance.png

---

# Business Value

The developed churn prediction system enables businesses to:

- Identify customers with a high probability of churn.
- Prioritize retention campaigns for at-risk customers.
- Reduce customer attrition and revenue loss.
- Improve customer lifetime value through proactive engagement.
- Optimize marketing expenditure by targeting the right customers.
- Support strategic decision-making using explainable machine learning models.
- Enable real-time churn prediction within the deployed Streamlit application.

---

# Conclusion

This phase successfully developed a complete end-to-end customer churn prediction pipeline using supervised machine learning.

Starting from engineered customer behavioural features, the project created a business-driven churn target, trained multiple classification algorithms, compared their performance, interpreted feature importance, and selected the Random Forest Classifier as the final production model.

The final model achieved an accuracy of **85.37%** with a **ROC-AUC score of 0.9376**, demonstrating strong predictive capability while remaining interpretable through feature importance and permutation importance analysis.

All preprocessing components, feature metadata, and trained models were serialized and stored for deployment. The resulting churn prediction pipeline is production-ready and will be integrated into the Streamlit dashboard to provide real-time customer churn predictions and support data-driven customer retention strategies.