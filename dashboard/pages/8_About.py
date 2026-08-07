"""
About Page
------------------------------------------------------------

What this project is, how it was built, and what each phase
of the pipeline does.

Project: Intelligent Customer Analytics Platform
"""

import streamlit as st

st.title("ℹ️ About This Project")

st.markdown(
    """
The **Intelligent Customer Analytics Platform** turns raw
e-commerce transaction data into customer-level insight: who the
customers are, what they're worth, who's likely to leave, and what
to recommend them next.

It's built on the **Online Retail** dataset — real transaction
records from a UK-based online gift retailer, covering
December 2009 to December 2011: roughly 800K transactions across
5,900+ customers and 40+ countries.
"""
)

st.divider()

# ==========================================================
# PIPELINE
# ==========================================================

st.header("🏗️ How It Was Built")

st.markdown(
    """
1. **Data Cleaning** — removed duplicates, handled missing customer
   IDs, and flagged cancelled orders (invoices starting with `C`)
   without discarding them.
2. **Feature Engineering** — built 31 customer-level behavioural
   features from the cleaned transactions: RFM (Recency, Frequency,
   Monetary), spending statistics, product diversity, cancellation
   patterns, and trend features comparing the first half of a
   customer's history to the second half.
3. **Customer Segmentation** — grouped customers with **K-Means
   clustering** on their RFM behaviour.
4. **CLV Prediction** — a **Gradient Boosting Regressor** predicts
   each customer's future lifetime value from their past behaviour.
5. **Churn Prediction** — a **Random Forest Classifier** predicts
   which customers are likely to stop buying (90+ days inactive).
   Four models were compared before picking Random Forest.
6. **Recommendation System** — combines popularity ranking,
   customer-based collaborative filtering, and item-based
   similarity to suggest products.
"""
)

st.divider()

# ==========================================================
# A NOTE ON THE CHURN MODEL
# ==========================================================

st.header("🔍 A Design Decision Worth Explaining")

st.markdown(
    """
The first version of the churn model scored **99.5% accuracy**.
That's a red flag, not a win: it turned out **Recency** (days since
last purchase) was in the feature set, and churn is *defined* by
recency being over 90 days — so the model was reading the answer
off a feature that encoded it, a classic case of **data leakage**.

Recency was removed and the model retrained on the remaining
behavioural features. Accuracy dropped to a realistic **~85%**,
which is the number actually reported on the Churn Prediction page.
"""
)

st.divider()

# ==========================================================
# TECH STACK
# ==========================================================

st.header("🧰 Tech Stack")

st.markdown(
    """
- **Data & ML:** pandas, NumPy, scikit-learn, XGBoost
- **Dashboard:** Streamlit, Plotly
- **Model persistence:** joblib
"""
)

st.divider()

st.caption(
    "Source code, notebooks, and a written report for every phase "
    "are available in the project repository."
)
