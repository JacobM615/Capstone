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
checkin_checkout = st.Page(
    "pages/checkin_checkout.py", title="Checkin-checkout history"
)
subscriptions = st.Page("pages/subscriptions.py", title="Subscriptions")

navigation = st.navigation(
    [home_page, checkin_checkout, subscriptions], expanded=True
)
navigation.run()
