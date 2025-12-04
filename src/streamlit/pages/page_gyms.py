import streamlit as st
import pandas as pd
import plotly.express as px
import os

from src.etl.utils.file_utils import find_root

st.markdown(
    "<h1 style='text-align: center;'>Gyms</h1>",
    unsafe_allow_html=True,
)

checkin_checkout = pd.read_csv(
    str(
        os.path.join(
            find_root(),
            "data",
            "output",
            "single_tables",
            "checkin_checkout.csv",
        )
    )
)

checkin_checkout__gyms__users = pd.read_csv(
    str(
        os.path.join(
            find_root(),
            "data",
            "output",
            "merged",
            "checkin_checkout__gyms__users.csv",
        )
    )
)

st.subheader("Number of visits vs gym")
gym_id_counts = (
    checkin_checkout["gym_id"]
    .value_counts()
    .rename_axis("gym_id")
    .reset_index(name="Number of workouts")
)

fig_gym_id = px.bar(
    gym_id_counts,
    x="gym_id",
    y="Number of workouts",
    color_discrete_sequence=["#ef4656"],
    labels={
        "gym_id": "Gym ID",
    },
)
fig_gym_id.update_yaxes(range=[29700, 30200])

st.plotly_chart(fig_gym_id)


def update_selected():
    if "All" in st.session_state.multi or (
        "Basic" in st.session_state.multi
        and "Pro" in st.session_state.multi
        and "Student" in st.session_state.multi
    ):
        st.session_state.multi = ["All"]


st.subheader("Number of visits vs gym type")

sub_plan_options = ["All"] + checkin_checkout__gyms__users[
    "subscription_plan"
].unique().tolist()
sub_plan_options = st.multiselect(
    "Select subscription plan:",
    sub_plan_options,
    key="multi",
    on_change=update_selected,
)

if st.session_state.multi != ["All"]:
    checkin_checkout__gyms__users_filtered = checkin_checkout__gyms__users[
        checkin_checkout__gyms__users["subscription_plan"].isin(
            st.session_state.multi
        )
    ]
else:
    checkin_checkout__gyms__users_filtered = checkin_checkout__gyms__users

if checkin_checkout__gyms__users_filtered.empty:
    st.warning("No subscription plans selected")
else:
    gym_type_counts = (
        checkin_checkout__gyms__users_filtered["gym_type"]
        .value_counts()
        .rename_axis("gym_type")
        .reset_index(name="Number of visits")
    )

    fig_gym_type = px.bar(
        gym_type_counts,
        x="gym_type",
        y="Number of visits",
        color_discrete_sequence=["#ef4656"],
        labels={
            "gym_type": "Gym type",
        },
    )
    fig_gym_type.update_yaxes(range=[0, 150000])

    st.plotly_chart(fig_gym_type)
