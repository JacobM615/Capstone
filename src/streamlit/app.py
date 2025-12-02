import streamlit as st

st.set_page_config(
    page_title="Gym data capstone",
    layout="wide",
    initial_sidebar_state="expanded",
)

with open("style_sheet.css") as css:
    css_content = css.read()

st.markdown(
    f"""
    <style>
    {css_content}
    </style>
    """,
    unsafe_allow_html=True,
)

home_page = st.Page("pages/page_home.py", title="Homepage")
second_page = st.Page("pages/page_2.py", title="Page 2")

navigation = st.navigation([home_page, second_page])
navigation.run()
