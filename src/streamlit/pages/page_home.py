import streamlit as st

st.title("Home Page")  # Or st.header()??

st.subheader("Please you the sidebar navigation to explore the dataset!")

url = "https://www.kaggle.com/datasets/mexwell/gym-check-ins-and-user-metadata"
st.markdown(
    "The dataset in question is a modified version of: [link](%s)" % url
)
