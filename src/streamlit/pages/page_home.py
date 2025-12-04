import streamlit as st

st.markdown(
    "<h1 style='text-align: center;'>Home Page</h1>",
    unsafe_allow_html=True,
)


st.subheader("Please you the sidebar navigation to explore the dataset!")

url = "https://www.kaggle.com/datasets/mexwell/gym-check-ins-and-user-metadata"
st.markdown(
    "The dataset in question is a modified version of: [link](%s)" % url
)
