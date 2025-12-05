import streamlit as st
import pandas as pd
import plotly.express as px
import os

from src.etl.utils.file_utils import find_root

st.markdown(
    "<h1 style='text-align: center;'>Workouts</h1>",
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
st.subheader("Number of workouts vs workout type")
workout_type_counts = (
    checkin_checkout["workout_type"]
    .value_counts()
    .rename_axis("workout_type")
    .reset_index(name="Number of workouts")
)

fig_workout_type = px.bar(
    workout_type_counts,
    x="workout_type",
    y="Number of workouts",
    color_discrete_sequence=["#ef4656"],
    labels={
        "workout_type": "Workout types",
    },
)
fig_workout_type.update_yaxes(range=[49300, 50200])

st.plotly_chart(fig_workout_type)

st.subheader("Number of workouts per user")
user_id_counts = (
    checkin_checkout["user_id"]
    .value_counts()
    .rename_axis("user_id")
    .reset_index(name="Number of workouts")
)

fig_user_id = px.scatter(
    user_id_counts,
    x="user_id",
    y="Number of workouts",
    color_discrete_sequence=["#ef4656"],
    labels={
        "user_id": "User ID",
    },
)
fig_user_id.update_yaxes(range=[30, 90])

st.plotly_chart(fig_user_id)

st.subheader("Histogram of workout durations")
bin_options = ["Small", "Medium", "Large"]
bin_selected = st.selectbox("Select a bin size..", bin_options)
checkin_checkout = checkin_checkout.astype({"duration": "timedelta64[ns]"})
checkin_checkout["duration"] = checkin_checkout["duration"] / pd.Timedelta(
    "1 hour"
)
if bin_selected == "Small":
    bins = 180
elif bin_selected == "Medium":
    bins = 100
elif bin_selected == "Large":
    bins = 20

fig_duration = px.histogram(
    checkin_checkout.sort_values(by=["duration"]),
    x="duration",
    nbins=bins,
    color_discrete_sequence=["#ef4656"],
    labels={
        "duration": "Workout duration / hours",
    },
)
fig_duration.update_layout(yaxis_title="Number of workouts")

st.plotly_chart(fig_duration)
