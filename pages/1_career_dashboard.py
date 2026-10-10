import streamlit as st
import pandas as pd

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Career Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD DATA ----------------

data = pd.read_csv("dataset.csv")

# ---------------- TITLE ----------------

st.title("📊 Career Dashboard")

st.write(
    "Explore the career categories available in the AI Career Guidance System."
)

st.divider()

# ---------------- METRICS ----------------

total_students = len(data)
total_careers = data["Career"].nunique()
average_cgpa = round(data["CGPA"].mean(), 2)
average_projects = round(data["Projects"].mean(), 2)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👩‍🎓 Students", total_students)

with col2:
    st.metric("🎯 Career Options", total_careers)

with col3:
    st.metric("📚 Average CGPA", average_cgpa)

with col4:
    st.metric("💻 Avg. Projects", average_projects)

st.divider()

# ---------------- CAREER DISTRIBUTION ----------------

st.subheader("🎯 Career Distribution")

career_count = data["Career"].value_counts()

st.bar_chart(career_count)

# ---------------- CAREER TABLE ----------------

st.subheader("📋 Career Summary")

career_summary = (
    data.groupby("Career")
    .agg(
        Students=("Career", "count"),
        Average_CGPA=("CGPA", "mean"),
        Average_Projects=("Projects", "mean"),
        Average_Certifications=("Certifications", "mean")
    )
    .round(2)
    .reset_index()
)

st.dataframe(
    career_summary,
    use_container_width=True,
    hide_index=True
)

# ---------------- SKILL ANALYSIS ----------------

st.subheader("💻 Skill Overview")

skill_data = pd.DataFrame({
    "Skill": [
        "Python",
        "Java",
        "SQL",
        "Machine Learning"
    ],
    "Students": [
        data["Python"].sum(),
        data["Java"].sum(),
        data["SQL"].sum(),
        data["Machine_Learning"].sum()
    ]
})

st.bar_chart(
    skill_data.set_index("Skill")
)

# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "AI-Based Career Guidance System | Career Dashboard"
)
