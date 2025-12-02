import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px
import os

from src.etl.utils.file_utils import find_root

st.title("Home Page")  # Or st.header()??


checkin_checkout = pd.read_csv(
    str(
        os.path.join(
            find_root(),
            "data",
            "output",
            "checkin_checkout.csv",
        )
    )
)

workout_type_counts = (
    checkin_checkout["workout_type"]
    .value_counts()
    .rename_axis("workout_type")
    .reset_index(name="counts")
)

chart = (
    alt.Chart(workout_type_counts)
    .mark_bar()
    .encode(
        y=alt.Y("counts", scale=alt.Scale(domain=[49200, 50400], clamp=True)),
        x=alt.X("workout_type", sort="y"),
    )
)

st.altair_chart(chart)
