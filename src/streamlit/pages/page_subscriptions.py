import streamlit as st
import pandas as pd
import plotly.express as px
import os

from src.etl.utils.file_utils import find_root


st.markdown(
    "<h1 style='text-align: center;'>Subscription plans</h1>",
    unsafe_allow_html=True,
)

users__sub_plans = pd.read_csv(
    str(
        os.path.join(
            find_root(),
            "data",
            "output",
            "merged",
            "users__sub_plans.csv",
        )
    )
)

st.subheader("Number of subscriptions vs subscription plan")
age_range = st.slider("(filtered by age range)", 18, 64, (18, 64))
users__sub_plans_filtered = users__sub_plans[
    (users__sub_plans["age"] >= age_range[0])
    & (users__sub_plans["age"] <= age_range[1])
]

sub_plans_counts = (
    users__sub_plans_filtered["subscription_plan"]
    .value_counts()
    .sort_values(ascending=True)
)

fig_sub_plans_counts = px.bar(
    sub_plans_counts,
    color_discrete_sequence=["#ef4656"],
    labels={
        "value": "Number of subscriptions",
        "subscription_plan": "Subscription plans",
    },
)

fig_sub_plans_counts.update_yaxes(
    range=[sub_plans_counts.min() - 20, sub_plans_counts.max() + 20]
)
fig_sub_plans_counts.update_layout(showlegend=False)
st.plotly_chart(fig_sub_plans_counts)


sub_plans_sums = (
    users__sub_plans_filtered.groupby("subscription_plan")["price_per_month"]
    .sum()
    .to_frame()
    .reset_index()
    .rename({"price_per_month": "price_per_month sum"}, axis=1)
    .sort_values("price_per_month sum", ascending=False)
)

fig_sub_plans_sums = px.bar(
    sub_plans_sums,
    x="subscription_plan",
    y="price_per_month sum",
    color_discrete_sequence=["#ef4656"],
    labels={
        "price_per_month sum": "Revenue per month",
        "subscription_plan": "Subscription plans",
    },
)

fig_sub_plans_sums.update_yaxes(range=[0, 85000])
st.subheader("Revenue per month vs subscription plan")
st.plotly_chart(fig_sub_plans_sums)
