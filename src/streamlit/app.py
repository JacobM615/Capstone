import streamlit as st

st.set_page_config(
    page_title="Gym data capstone",
    # layout="wide",
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
workouts = st.Page("pages/page_workouts.py", title="Workouts")
subscriptions = st.Page("pages/page_subscriptions.py", title="Subscriptions")
gyms = st.Page("pages/page_gyms.py", title="Gyms")
# testing = st.Page("pages/testing_page.py", title="TESTING")

navigation = st.navigation(
    [home_page, workouts, subscriptions, gyms], expanded=True
)
navigation.run()
