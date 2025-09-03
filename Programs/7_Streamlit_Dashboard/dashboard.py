import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Pakistan Education & Population Analysis Dashboard")

pages = {
    "Options": [
        st.Page("population.py", title="Population"),
        st.Page("skills.py", title="Skills"),
    ],
}

pg = st.navigation(pages)
pg.run()