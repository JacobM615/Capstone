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
fig_gym_id.update_yaxes(range=[29700, 30300])

st.plotly_chart(fig_gym_id)
