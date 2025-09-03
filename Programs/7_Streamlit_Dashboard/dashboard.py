import streamlit as st

st.set_page_config(
    page_title="Pakistan Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("📊 Pakistan Education & Population Analysis Dashboard")

pages = {
    "Options": [
        st.Page("population.py", title="Population"),
        st.Page("skills.py", title="Skills"),
    ],
}

pg = st.navigation(pages)

pg.run()


