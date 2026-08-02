# Phase 5: Customer Segmentation

## Objective

The objective of this phase is to segment customers into meaningful groups based on their purchasing behaviour using **unsupervised machine learning**.

Unlike supervised learning, where target labels are already known, customer segmentation discovers hidden patterns within the data by grouping customers with similar characteristics.

The generated customer segments enable businesses to:

- Understand different customer behaviours.
- Personalize marketing campaigns.
- Improve customer retention.
- Increase customer lifetime value.
- Support data-driven business decision making.

The output of this phase is a customer-level dataset containing cluster labels and business-friendly customer segment names.

---

# Input

```
data/processed/customer_features.csv
```

This dataset was generated during **Phase 4 (Feature Engineering)** and contains customer-level behavioural features.

---

# Output

```
data/processed/customer_segments.csv
```

Additional outputs generated in this phase:

```
data/processed/cluster_profile.csv

data/processed/business_segment_summary.csv
```

Figures generated:

```
reports/figures/elbow_curve.png

reports/figures/silhouette_scores.png

reports/figures/customer_segments.png

reports/figures/revenue_by_segment.png
```

---

# Sections Completed

---

## 1. Load Customer Feature Dataset

The engineered customer feature dataset was loaded into a DataFrame and validated.

Validation included:

- Dataset dimensions
- Data types
- Missing value analysis
- Customer count verification

Purpose:

Ensure the engineered features are complete before applying clustering algorithms.

---

## 2. Feature Overview

The dataset was inspected to identify:

- Numerical features
- Categorical features

The following columns were excluded from clustering:

- CustomerID
- Country

These columns are identifiers or categorical information and do not contribute to distance-based clustering.

Purpose:

Prepare the feature matrix for machine learning.

---

## 3. Correlation Analysis

Correlation analysis was performed on all numerical features.

Analysis included:

- Correlation matrix
- Heatmap visualization
- Highly correlated feature inspection

Purpose:

Understand relationships among engineered features and identify redundant information.

---

## 4. Feature Scaling

Since clustering algorithms rely on Euclidean distance, all numerical features were standardized using:

- StandardScaler

The transformed feature matrix was stored as:

```
X_scaled
```

Purpose:

Ensure that all features contribute equally to the clustering process regardless of their original scales.

---

## 5. Principal Component Analysis (PCA)

Principal Component Analysis (PCA) was applied to reduce the high-dimensional feature space into two principal components.

Generated:

- PC1
- PC2

Purpose:

Visualize customer segments in two dimensions while preserving as much variance as possible.

---

## 6. Determine the Optimal Number of Clusters

The optimal number of clusters was evaluated using two methods:

### Elbow Method

Measured the Within-Cluster Sum of Squares (WCSS) for different values of K.

### Silhouette Score

Measured the quality of clustering by evaluating cluster separation.

After comparing both methods, the final choice was:

```
Number of Clusters = 4
```

Reason:

Although the Silhouette Score was highest for K=2, the Elbow Method and business interpretability indicated that four customer segments provide more meaningful business insights.

---

## 7. K-Means Clustering

The K-Means clustering algorithm was applied using:

- K = 4
- Random State = 42

Generated:

- Cluster labels
- Cluster distribution
- Cluster centers

Purpose:

Group customers with similar purchasing behaviour into distinct customer segments.

---

## 8. Cluster Profiling

Average values of all customer features were calculated for each cluster.

Generated:

```
cluster_profile.csv
```

This profile summarizes:

- Spending behaviour
- Purchase frequency
- Product diversity
- Revenue
- Purchase activity
- Cancellation behaviour

Purpose:

Interpret the characteristics of each customer segment.

---

## 9. Cluster Visualization

Several visualizations were created to understand the segmentation results.

Generated visualizations:

- PCA Cluster Projection
- Revenue by Cluster
- Frequency by Cluster
- Recency by Cluster
- Customer Count by Cluster

Purpose:

Provide an intuitive understanding of how customers are distributed across different segments.

---

## 10. Business Insights

The numerical cluster labels were translated into meaningful business segments.

Final customer segments:

### VIP Customers

Characteristics:

- Highest spending
- Highest purchase frequency
- Highly loyal
- Small customer base with significant revenue contribution

Business Strategy:

- Loyalty programs
- Premium memberships
- Early product access
- Exclusive rewards

---

### Regular Customers

Characteristics:

- Largest active customer group
- Moderate purchase frequency
- Moderate revenue contribution

Business Strategy:

- Cross-selling
- Upselling
- Personalized recommendations
- Seasonal marketing campaigns

---

### Exceptional High-Value Customer

Characteristics:

- Single customer with extremely high spending
- Behaves differently from all other customers
- Represents an outlier in the dataset

Business Strategy:

- Individual monitoring
- Dedicated relationship management
- Verify transaction validity

---

### At-Risk Customers

Characteristics:

- Low spending
- Very low purchase frequency
- High recency (inactive customers)

Business Strategy:

- Re-engagement campaigns
- Discount offers
- Win-back emails
- Retention marketing

---

## 11. Save Final Results

The final customer segmentation dataset was saved.

Generated datasets:

```
customer_segments.csv

cluster_profile.csv

business_segment_summary.csv
```

These datasets will serve as the foundation for the remaining phases of the project.

---

# Final Dataset

The final dataset contains:

- Engineered customer features
- Cluster labels
- Business segment names

Each row represents a unique customer and their assigned customer segment.

---

# Business Value

Customer segmentation transforms historical transaction data into actionable business intelligence.

The generated customer segments enable businesses to:

- Personalize customer experiences.
- Improve marketing effectiveness.
- Increase customer retention.
- Allocate marketing resources efficiently.
- Identify high-value customers.
- Detect inactive customers requiring re-engagement.

These insights form the foundation for advanced predictive analytics in subsequent phases.

---

# Key Learnings

During this phase, the following concepts were applied:

- Unsupervised Machine Learning
- K-Means Clustering
- Feature Scaling
- Principal Component Analysis (PCA)
- Elbow Method
- Silhouette Score
- Cluster Profiling
- Customer Behaviour Analysis
- Business Interpretation of Machine Learning Results

---

# Conclusion

In this phase, customers were successfully segmented into four meaningful groups based on their purchasing behaviour.

The segmentation process converted complex behavioural data into interpretable business insights, enabling targeted marketing strategies and improved customer relationship management.

The resulting segmented dataset will be used as a key input for the upcoming phases, including Customer Lifetime Value (CLV) Prediction, Churn Prediction, Product Recommendation System, Dashboard Development, and Deployment.