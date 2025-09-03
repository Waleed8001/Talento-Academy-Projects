import streamlit as st
import plotly.express as px
import nbformat

# =====================
# Dataset Overview
# =====================
total_population = 255.86
female_literacy = 65.19
youth = 74.2
middle_class = 45
lower_middle_class = 88
schooling = 45.90
intermediate = 2.56
university = 1.95
study_discontinued = 49

def chart4_mc_education():
    total_education = schooling + intermediate + university + study_discontinued
    middle_class_youth = (middle_class / (middle_class + lower_middle_class)) * youth

    mc_schooling = (schooling / total_education) * middle_class_youth
    mc_intermediate = (intermediate / total_education) * middle_class_youth
    mc_university = (university / total_education) * middle_class_youth
    mc_discontinued = (study_discontinued / total_education) * middle_class_youth

    values = [mc_schooling, mc_intermediate, mc_university, mc_discontinued]
    labels = [
        f"Schooling ({mc_schooling:.2f}M)",
        f"Intermediate ({mc_intermediate:.2f}M)",
        f"University ({mc_university:.2f}M)",
        f"Study Discontinued ({mc_discontinued:.2f}M)"
    ]

    fig = px.pie(values=values, labels=labels, names=labels)
    st.plotly_chart(fig, key="education middle class")

def chart5_lmc_education():
    total_education = schooling + intermediate + university + study_discontinued
    lower_middle_class_youth = (lower_middle_class / (middle_class + lower_middle_class)) * youth

    lmc_schooling = (schooling / total_education) * lower_middle_class_youth
    lmc_intermediate = (intermediate / total_education) * lower_middle_class_youth
    lmc_university = (university / total_education) * lower_middle_class_youth
    lmc_discontinued = (study_discontinued / total_education) * lower_middle_class_youth

    values = [lmc_schooling, lmc_intermediate, lmc_university, lmc_discontinued]
    labels = [
        f"Schooling ({lmc_schooling:.2f}M)",
        f"Intermediate ({lmc_intermediate:.2f}M)",
        f"University ({lmc_university:.2f}M)",
        f"Study Discontinued ({lmc_discontinued:.2f}M)"
    ]

    fig = px.pie(values=values, labels=labels, names=labels)
    st.plotly_chart(fig, key="education lower middle class")
    
    
col1, col2 = st.columns(2)

with col1:
    st.subheader("Education Breakdown of Middle Class Youth")
    chart4_mc_education()
    
    st.subheader("Education Breakdown of Lower Middle Class Youth")
    chart5_lmc_education()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # fig, ax = plt.subplots(figsize=(7,7))
    # ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140,
    #        colors=["#66b3ff","#99ff99","#ffcc99","#ff9999"])
    # ax.set_title("Education Breakdown of Youth in Middle Class")
    # st.pyplot(fig)
    # fig, ax = plt.subplots(figsize=(7,7))
    # ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140,
    #        colors=["#66b3ff","#99ff99","#ffcc99","#ff9999"])
    # ax.set_title("Education Breakdown of Youth in Lower Middle Class")

    # st.pyplot(fig)
