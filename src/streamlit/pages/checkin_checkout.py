import streamlit as st
import pandas as pd
import plotly.express as px
import os

from src.etl.utils.file_utils import find_root

st.title("Checkin_checkout_history")


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

workout_type_counts = (
    checkin_checkout["workout_type"]
    .value_counts()
    .rename_axis("workout_type")
    .reset_index(name="Number of workouts")
)

fig_workout_type = px.bar(
    workout_type_counts, x="workout_type", y="Number of workouts"
)
fig_workout_type.update_yaxes(range=[49300, 50200])

st.plotly_chart(fig_workout_type)


gym_id_counts = (
    checkin_checkout["gym_id"]
    .value_counts()
    .rename_axis("gym_id")
    .reset_index(name="Number of workouts")
)

fig_gym_id = px.bar(gym_id_counts, x="gym_id", y="Number of workouts")
fig_gym_id.update_yaxes(range=[29700, 30300])

st.plotly_chart(fig_gym_id)


user_id_counts = (
    checkin_checkout["user_id"]
    .value_counts()
    .rename_axis("user_id")
    .reset_index(name="Number of workouts")
)

fig_user_id = px.scatter(user_id_counts, x="user_id", y="Number of workouts")
fig_user_id.update_yaxes(range=[30, 90])

st.plotly_chart(fig_user_id)


checkin_checkout = checkin_checkout.astype({"duration": "timedelta64[ns]"})
fig_duration = px.histogram(
    checkin_checkout.sort_values(by=["duration"]), x="duration", nbins=110
)

st.plotly_chart(fig_duration)
