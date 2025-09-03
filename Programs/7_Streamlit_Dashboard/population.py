import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
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

categories = [
    "Female Literacy Rate",
    "Youth (15–25)",
    "Middle Class",
    "Lower Middle Class",
    "Schooling",
    "Intermediate Education",
    "University Education",
    "Study Discontinued"
]
values = [
    female_literacy,
    youth,
    middle_class,
    lower_middle_class,
    schooling,
    intermediate,
    university,
    study_discontinued
]

# =====================
# Helper Functions for Charts
# =====================

# Chart 1
def chart1_total_population(categories, values):
    labels = []
    for c, v in zip(categories, values):
        labels.append(f"{c} ({v}M)")
            
    df = px.pie(values=values, labels=labels, names=categories)
    st.plotly_chart(df, key="total_population")
    

# Chart 2
def chart2_youth_vs_population(total_population, youth):    
    remaining_population = total_population - youth
    values = [youth, remaining_population]
    labels = [f"Youth (15–25) ({youth}M)", f"Remaining ({remaining_population:.2f}M)"]
    

    names=["youth", "Remaining"]
    
    df = px.pie(values=values, labels=labels, names=names)
    st.plotly_chart(df, key="youth vs population")
    

# Chart 3
def chart3_youth_distribution():
    middle_class_youth = (middle_class / (middle_class + lower_middle_class)) * youth
    lower_middle_class_youth = (lower_middle_class / (middle_class + lower_middle_class)) * youth

    values = [middle_class_youth, lower_middle_class_youth]
    labels = [f"Middle Class Youth ({middle_class_youth:.2f}M)", f"Lower Middle Class Youth ({lower_middle_class_youth:.2f}M)"]
    
    df = px.pie(values=values, labels=labels, names=["Middle Class Youth", "Lower Middle Class Youth"])
    st.plotly_chart(df, key="youth distribution")
    
    
    
def bar_chart():
    st.subheader("Total Population")
    total_population = 255.86
    youth = 74.2
    
    categories = [
        "Female Literacy Rate",
        "Youth (15–25)",
        "Middle Class",
        "Lower Middle Class",
        "Schooling",
        "Intermediate Education",
        "University Education",
        "Study Discontinued"
    ]
    values = [
        female_literacy,
        youth,
        middle_class,
        lower_middle_class,
        schooling,
        intermediate,
        university,
        study_discontinued
    ]
    df = px.bar(x=categories, y=values)
    st.plotly_chart(df, key="total_population_bar")
    
    
    st.subheader("Youth vs Population")
    
    remaining_population = total_population - youth
    values = [youth, remaining_population]
    labels = [f"Youth (15–25) ({youth}M)", f"Remaining ({remaining_population:.2f}M)"]
    
    df_2 = px.bar(x=labels, y=values)
    st.plotly_chart(df_2, key="youth vs population_bar")
    
    
    st.subheader("Youth Distribution")
    
    middle_class_youth = (middle_class / (middle_class + lower_middle_class)) * youth
    lower_middle_class_youth = (lower_middle_class / (middle_class + lower_middle_class)) * youth

    values = [middle_class_youth, lower_middle_class_youth]
    labels = [f"Middle Class Youth ({middle_class_youth:.2f}M)", f"Lower Middle Class Youth ({lower_middle_class_youth:.2f}M)"]
    
    df_3 = px.bar(x=labels, y=values)
    st.plotly_chart(df_3, key="youth distribution_bar")
    
    
col1, col2 = st.columns(2)
with col1:
    st.subheader("Total Population")
    chart1_total_population(categories, values)
    st.subheader("Youth vs Population")
    chart2_youth_vs_population(total_population, youth)
    st.subheader("Youth Distribution")
    chart3_youth_distribution()

with col2:
    bar_chart()
    
















# labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
# values = [4500, 2500, 1053, 500]

# fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
# fig.show()

# df = px.data.iris()
# fig = px.scatter(df, x="sepal_width", y="sepal_length")

# event = st.plotly_chart(fig, key="iris", on_select="rerun")

# event

# df = px.data.iris()
# fig = px.scatter(
#     df,
#     x="sepal_width",
#     y="sepal_length",
#     color="species",
#     size="petal_length",
#     hover_data=["petal_width"],
# )

# event = st.plotly_chart(fig, key="iris", on_select="rerun")

# event.selection

    # fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    # # fig.show()
    # st.plotly_chart(fig, config = {'scrollZoom': True})
    
    
    
    
        # event.selection
    # fig, ax = plt.subplots(figsize=(7,7))
    # ax.pie(values, labels=[f"{c} ({v}M)" for c,v in zip(categories, values)], autopct='%1.1f%%', startangle=140)
    # ax.set_title("Total Population Breakdown (255.86M)")
    # st.pyplot(fig)

    # event.selection
    # print(labels)
    # print(values)
    # fig, ax = plt.subplots(figsize=(7,7))
    # ax.pie(values, labels=[f"{c} ({v}M)" for c,v in zip(categories, values)], autopct='%1.1f%%', startangle=140)
    # ax.set_title("Total Population Breakdown (255.86M)")
    # st.pyplot(fig)
    # print(5)
    # print(values, labels)
    # fig, ax = plt.subplots(figsize=(6,6))
    # fig, ax = plt.subplots(figsize=(6,6))
    # ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=["#66b3ff","#ff9999"])
    # ax.set_title("Youth vs Total Population")
    # st.pyplot(fig)
    # ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=["#99ff99","#ffcc99"])
    # ax.set_title("Youth Distribution in Middle and Lower Middle Class")
    # st.pyplot(fig)