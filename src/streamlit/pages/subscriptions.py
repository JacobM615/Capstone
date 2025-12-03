import streamlit as st
import pandas as pd
import plotly.express as px
import os

from src.etl.utils.file_utils import find_root

# from src.streamlit.app import age_range

st.title("Subscription_plans")


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


# sub_plans_counts = (
#     users__sub_plans.groupby("subscription_plan")["user_id"]
#     .count()
#     .to_frame()
#     .reset_index()
#     .rename({"user_id": "user_id count"}, axis=1)
#     .sort_values("user_id count", ascending=False)
# )

# fig_sub_plans_counts = px.bar(
#     sub_plans_counts,
#     x="subscription_plan",
#     y="user_id count",
# )

# fig_sub_plans_counts.update_yaxes(range=[1600, 1700])

# st.plotly_chart(fig_sub_plans_counts)

age_range = st.slider("Select an age range", 18, 64, (18, 64))
print(age_range)
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
)

fig_sub_plans_counts.update_yaxes(
    range=[sub_plans_counts.min() - 50, sub_plans_counts.max() + 50]
)

st.plotly_chart(fig_sub_plans_counts)


sub_plans_sums = (
    users__sub_plans.groupby("subscription_plan")["price_per_month"]
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
)

fig_sub_plans_sums.update_yaxes(range=[0, 85000])

st.plotly_chart(fig_sub_plans_sums)
