"""
Customer Churn Prediction Dashboard
------------------------------------------------------------

Loads the trained Random Forest model (Phase 7) and scores every
customer in the feature dataset (Phase 4) live, in the app.

A customer is labelled "churned" if they have not purchased in the
last 90 days. That label is used only to train the model — it is
never shown to the model as an input feature.

Project: Intelligent Customer Analytics Platform
"""

import joblib
import pandas as pd
import plotly.express as px
import streamlit as st

from utils.cache import load_csv
from utils.config import (
    CHURN_FEATURE_LIST_PATH,
    CHURN_MODEL_INFO_PATH,
    CHURN_MODEL_PATH,
    PROCESSED_DATA_DIR,
)
from utils.helper import format_currency

CHURN_WINDOW_DAYS = 90

# ==========================================================
# LOAD MODEL + DATA
# ==========================================================

@st.cache_resource(show_spinner=False)
def load_churn_artifacts():
    model = joblib.load(CHURN_MODEL_PATH)
    feature_list = joblib.load(CHURN_FEATURE_LIST_PATH)
    model_info = joblib.load(CHURN_MODEL_INFO_PATH)
    return model, feature_list, model_info


@st.cache_data(show_spinner=False)
def score_customers(_model, feature_list):
    """
    Load the customer feature table, build the churn label, and
    score every customer with the trained model.
    """

    df = load_csv(
        PROCESSED_DATA_DIR / "customer_features.csv"
    )

    df["Churn"] = (
        df["Recency"] > CHURN_WINDOW_DAYS
    ).astype(int)

    # Same encoding used to train the model: countries mapped to
    # an integer code in sorted alphabetical order.
    country_mapping = {
        country: code
        for code, country in enumerate(sorted(df["Country"].unique()))
    }

    X = df.drop(columns=["CustomerID", "Recency", "Churn"]).copy()
    X["Country"] = X["Country"].map(country_mapping)
    X = X[feature_list]

    df["ChurnProbability"] = _model.predict_proba(X)[:, 1]
    df["PredictedChurn"] = _model.predict(X)

    df["RiskCategory"] = pd.cut(
        df["ChurnProbability"],
        bins=[-0.01, 0.4, 0.7, 1.0],
        labels=["Low Risk", "Medium Risk", "High Risk"],
    )

    return df


model, feature_list, model_info = load_churn_artifacts()
scored_df = score_customers(model, feature_list)

RISK_COLORS = {
    "High Risk": "#e74c3c",
    "Medium Risk": "#f1c40f",
    "Low Risk": "#2ecc71",
}

# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("⚠️ Customer Churn Prediction")

st.markdown(
    f"""
A customer is defined as **churned** if they haven't purchased
anything in the last **{CHURN_WINDOW_DAYS} days**. The model below
was trained on customer purchase behaviour (frequency, spend,
product variety, cancellations, etc.) to predict that outcome
*before* it happens, so at-risk customers can be targeted early.
"""
)

with st.expander("ℹ️ A note on model accuracy"):
    st.markdown(
        """
An earlier version of this model used **Recency** (days since last
purchase) directly as an input feature. Since churn is *defined* by
recency, the model could essentially read the answer off the
question — it scored **99.5% accuracy**, which was a red flag for
data leakage rather than a genuinely strong model.

Recency was removed from the feature set and the model was
retrained on the remaining behavioural features. Accuracy dropped
to **~85%**, which is a realistic, trustworthy number for this
problem.
"""
    )

st.divider()

# ==========================================================
# MODEL PERFORMANCE (from the held-out test set)
# ==========================================================

st.header("📈 Model Performance")

st.caption(
    "Random Forest was the best of 4 models tried (Logistic Regression, "
    "Decision Tree, Random Forest, XGBoost), measured on a 20% held-out "
    "test set the model never saw during training."
)

m1, m2, m3, m4, m5 = st.columns(5)

m1.metric("Accuracy", f"{model_info['Accuracy']:.1%}")
m2.metric("Precision", f"{model_info['Precision']:.1%}")
m3.metric("Recall", f"{model_info['Recall']:.1%}")
m4.metric("F1 Score", f"{model_info['F1 Score']:.1%}")
m5.metric("ROC-AUC", f"{model_info['ROC-AUC']:.3f}")

st.caption(
    "**Precision** — of the customers flagged as likely to churn, how "
    "many actually did. **Recall** — of the customers who actually "
    "churned, how many the model caught."
)

st.divider()

# ==========================================================
# BUSINESS OVERVIEW
# ==========================================================

st.header("📌 Churn Risk Across All Customers")

total_customers = len(scored_df)
predicted_churn = int(scored_df["PredictedChurn"].sum())
retained = total_customers - predicted_churn
avg_probability = scored_df["ChurnProbability"].mean()

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Customers", f"{total_customers:,}")
k2.metric("Predicted to Churn", f"{predicted_churn:,}")
k3.metric("Predicted to Stay", f"{retained:,}")
k4.metric("Avg. Churn Probability", f"{avg_probability:.1%}")

chart_col, table_col = st.columns([1, 1])

with chart_col:
    risk_counts = (
        scored_df["RiskCategory"]
        .value_counts()
        .reindex(["Low Risk", "Medium Risk", "High Risk"])
        .reset_index()
    )
    risk_counts.columns = ["RiskCategory", "Customers"]

    fig_risk = px.pie(
        risk_counts,
        names="RiskCategory",
        values="Customers",
        hole=0.45,
        color="RiskCategory",
        color_discrete_map=RISK_COLORS,
    )
    fig_risk.update_layout(height=340, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_risk, use_container_width=True)

with table_col:
    risk_summary = (
        scored_df.groupby("RiskCategory", observed=True)
        .agg(
            Customers=("CustomerID", "count"),
            AvgProbability=("ChurnProbability", "mean"),
            AvgMonetary=("Monetary", "mean"),
        )
        .round(2)
        .reset_index()
    )
    st.dataframe(risk_summary, use_container_width=True, hide_index=True)

st.caption(
    "Risk tiers: **Low** (<40% churn probability), **Medium** (40–70%), "
    "**High** (>70%)."
)

st.divider()

# ==========================================================
# WHAT DRIVES CHURN
# ==========================================================

st.header("⚙️ What Drives Churn Risk")

importance_df = pd.DataFrame(
    {
        "Feature": feature_list,
        "Importance": model.feature_importances_,
    }
).sort_values("Importance", ascending=False).head(10)

fig_importance = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
)
fig_importance.update_layout(
    height=380,
    yaxis=dict(autorange="reversed"),
    margin=dict(l=10, r=10, t=10, b=10),
)
st.plotly_chart(fig_importance, use_container_width=True)

st.caption(
    "These are the features the Random Forest relied on most to tell "
    "churned customers apart from retained ones — mainly how a "
    "customer's spending and buying frequency are trending over time, "
    "and how long their purchase history spans."
)

st.divider()

# ==========================================================
# CUSTOMER LOOKUP
# ==========================================================

st.header("👤 Look Up a Customer")

selected_customer = st.selectbox(
    "Customer ID",
    sorted(scored_df["CustomerID"].unique()),
)

customer = scored_df[
    scored_df["CustomerID"] == selected_customer
].iloc[0]

c1, c2, c3 = st.columns(3)
c1.metric("Country", customer["Country"])
c2.metric("Churn Probability", f"{customer['ChurnProbability']:.1%}")
c3.metric("Risk Category", customer["RiskCategory"])

st.caption(
    f"**Frequency:** {customer['Frequency']:.0f} orders  •  "
    f"**Monetary value:** {format_currency(customer['Monetary'])}  •  "
    f"**Recency:** {customer['Recency']:.0f} days since last purchase"
)

st.divider()

# ==========================================================
# TRY YOUR OWN CUSTOMER
# ==========================================================

st.header("🧮 Try Your Own Customer")

st.caption(
    "Adjust the values below and the trained model will score this "
    "customer live. Fields not shown here are filled in with the "
    "dataset median."
)

country_mapping = {
    country: code
    for code, country in enumerate(sorted(scored_df["Country"].unique()))
}
default_row = scored_df[feature_list].median(numeric_only=True)
default_row["Country"] = country_mapping[scored_df["Country"].mode()[0]]
default_row = default_row[feature_list]

i1, i2, i3 = st.columns(3)

with i1:
    in_frequency = st.number_input("Frequency (orders)", value=5.0, min_value=0.0)
    in_monetary = st.number_input("Monetary value", value=1000.0, min_value=0.0)

with i2:
    in_purchase_span = st.number_input("Purchase span (days)", value=180.0, min_value=0.0)
    in_active_months = st.number_input("Active months", value=6.0, min_value=0.0)

with i3:
    in_purchase_trend = st.slider("Purchase trend (2nd half vs 1st half)", -1.0, 1.0, 0.0)
    in_revenue_trend = st.slider("Revenue trend (2nd half vs 1st half)", -1.0, 1.0, 0.0)

if st.button("Predict Churn Risk"):

    trial_row = default_row.copy()
    trial_row["Frequency"] = in_frequency
    trial_row["Monetary"] = in_monetary
    trial_row["PurchaseSpan"] = in_purchase_span
    trial_row["ActiveMonths"] = in_active_months
    trial_row["PurchaseTrend"] = in_purchase_trend
    trial_row["RevenueTrend"] = in_revenue_trend

    trial_X = pd.DataFrame([trial_row])[feature_list]
    trial_probability = model.predict_proba(trial_X)[0, 1]

    if trial_probability >= 0.7:
        tier, tone = "High Risk", st.error
    elif trial_probability >= 0.4:
        tier, tone = "Medium Risk", st.warning
    else:
        tier, tone = "Low Risk", st.success

    r1, r2 = st.columns(2)
    r1.metric("Predicted Churn Probability", f"{trial_probability:.1%}")
    r2.metric("Risk Category", tier)
    tone(f"This customer falls into the **{tier}** category.")

st.divider()

# ==========================================================
# RETENTION PLAYBOOK
# ==========================================================

st.header("❤️ Retention Playbook")

r1, r2, r3 = st.columns(3)

with r1:
    st.error(
        "**High Risk**\n\n- Personal outreach\n- Win-back discount\n- Priority support"
    )

with r2:
    st.warning(
        "**Medium Risk**\n\n- Targeted email campaign\n- Engagement nudge"
    )

with r3:
    st.success(
        "**Low Risk**\n\n- Maintain current experience\n- Relevant upsells"
    )
