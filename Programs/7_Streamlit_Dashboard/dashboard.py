import streamlit as st

st.set_page_config(
    page_title="Pakistan Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
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

