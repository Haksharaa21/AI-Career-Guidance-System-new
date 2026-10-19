import streamlit as st
import pandas as pd
import joblib
import os

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------


st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.title("SIDEBAR TEST")
st.sidebar.success("Sidebar is working!")

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "career_model.pkl")
model = joblib.load(model_path)


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

with st.sidebar:
    st.title("🎓 Career Guidance")
    st.write("Machine Learning Based Career Recommendation")
    st.divider()
    st.page_link("app.py", label="Home", icon="🏠")
    st.page_link("pages/1_Career_Dashboard.py", label="Career Dashboard", icon="📊")
    st.page_link("pages/2_Skill_Gap_Analyzer.py", label="Skill Gap Analyzer", icon="🛠️")
    st.page_link("pages/3_Learning_Roadmap.py", label="Learning Roadmap", icon="🗺️")
    st.page_link("pages/4_Job_Market_Insights.py", label="Job Market Insights", icon="💼")
    st.page_link("pages/5_Career_Quiz.py", label="Career Quiz", icon="❓")
    st.page_link("pages/6_Resume_Builder.py", label="Resume Builder", icon="📝")
    st.page_link("pages/7_Resume_Analyzer.py", label="Resume Analyzer", icon="📄")

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

st.title("🎓 AI-Based Career Guidance System")

st.write(
    "An intelligent system that helps students identify suitable "
    "career paths based on their academic performance, technical "
    "skills, interests and experience."
)

st.divider()

# --------------------------------------------------
# WELCOME SECTION
# --------------------------------------------------

st.header("🌟 Welcome to AI Career Guidance")

st.write(
    "Choosing the right career can be challenging for students. "
    "This system uses Machine Learning to analyze student information "
    "and provide personalized career guidance."
)

# --------------------------------------------------
# PROJECT FEATURES
# --------------------------------------------------

st.subheader("✨ What This System Provides")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🎯\n\n**Career Prediction**\n\nPredict a suitable career.")

with col2:
    st.info("🛠️\n\n**Skill Gap Analysis**\n\nIdentify missing skills.")

with col3:
    st.info("🗺️\n\n**Learning Roadmap**\n\nFollow a career learning path.")

with col4:
    st.info("📄\n\n**Resume Analysis**\n\nAnalyze resume skills.")

st.divider()

# --------------------------------------------------
# HOW IT WORKS
# --------------------------------------------------

st.header("🔄 How the System Works")

step1, step2, step3, step4 = st.columns(4)

with step1:
    st.subheader("1️⃣ Enter Details")
    st.write(
        "Provide academic information, skills, "
        "interests and experience."
    )

with step2:
    st.subheader("2️⃣ ML Analysis")
    st.write(
        "The trained Machine Learning model "
        "analyzes the information."
    )

with step3:
    st.subheader("3️⃣ Career Prediction")
    st.write(
        "The system predicts suitable career "
        "options for the student."
    )

with step4:
    st.subheader("4️⃣ Guidance")
    st.write(
        "Explore skills, courses, roadmaps, "
        "projects and career comparisons."
    )

st.divider()

# --------------------------------------------------
# STUDENT INFORMATION
# --------------------------------------------------

st.header("👩‍🎓 Student Career Prediction")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=15,
        max_value=40,
        value=20
    )

    degree = st.selectbox(
        "Degree",
        [
            "BCA",
            "B.Sc CS",
            "B.Tech CSE",
            "B.Tech IT",
            "MCA"
        ]
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.5,
        step=0.1
    )

    python_skill = st.selectbox(
        "Python Skill",
        ["No", "Yes"]
    )

    java_skill = st.selectbox(
        "Java Skill",
        ["No", "Yes"]
    )

    sql_skill = st.selectbox(
        "SQL Skill",
        ["No", "Yes"]
    )

with col2:

    ml_skill = st.selectbox(
        "Machine Learning Skill",
        ["No", "Yes"]
    )

    communication = st.selectbox(
        "Communication Level",
        ["Low", "Medium", "High"]
    )

    problem_solving = st.selectbox(
        "Problem Solving Level",
        ["Low", "Medium", "High"]
    )

    interest = st.selectbox(
        "Career Interest",
        [
            "AI",
            "Cloud",
            "Cyber",
            "Data Science",
            "Software Development",
            "Web Development"
        ]
    )

    projects = st.number_input(
        "Number of Projects",
        min_value=0,
        max_value=20,
        value=1
    )

    certifications = st.number_input(
        "Number of Certifications",
        min_value=0,
        max_value=20,
        value=0
    )

# --------------------------------------------------
# MAPPINGS
# --------------------------------------------------

degree_map = {
    "BCA": 0,
    "B.Sc CS": 1,
    "B.Tech CSE": 2,
    "B.Tech IT": 3,
    "MCA": 4
}

interest_map = {
    "AI": 0,
    "Cloud": 1,
    "Cyber": 2,
    "Data Science": 3,
    "Software Development": 4,
    "Web Development": 5
}

skill_map = {
    "No": 0,
    "Yes": 1
}

level_map = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

st.divider()

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if st.button(
    "🔮 Predict My Career",
    use_container_width=True
):

    student = pd.DataFrame([[
        age,
        degree_map[degree],
        cgpa,
        skill_map[python_skill],
        skill_map[java_skill],
        skill_map[sql_skill],
        skill_map[ml_skill],
        level_map[communication],
        level_map[problem_solving],
        interest_map[interest],
        projects,
        certifications
    ]], columns=[
        "Age",
        "Degree",
        "CGPA",
        "Python",
        "Java",
        "SQL",
        "Machine_Learning",
        "Communication",
        "Problem_Solving",
        "Interest",
        "Projects",
        "Certifications"
    ])

    # Prediction
    prediction = model.predict(student)
    career = prediction[0]

    # Prediction probabilities
    probabilities = model.predict_proba(student)[0]
    classes = model.classes_

    results = pd.DataFrame({
        "Career": classes,
        "Confidence": probabilities
    })

    results = results.sort_values(
        by="Confidence",
        ascending=False
    )

    confidence = results.iloc[0]["Confidence"] * 100

    # --------------------------------------------------
    # RESULT
    # --------------------------------------------------

    st.success("✅ Prediction completed successfully!")

    st.header("🎯 Recommended Career")

    st.subheader(career)

    st.progress(int(confidence))

    st.write(
        f"**Model Confidence: {confidence:.2f}%**"
    )

    st.caption(
        "Model confidence indicates how strongly the trained model "
        "supports the prediction. It is not a guarantee of career success."
    )

    # --------------------------------------------------
    # CAREER DESCRIPTION
    # --------------------------------------------------

    career_info = {

        "AI Engineer":
        "AI Engineers develop intelligent applications using "
        "Artificial Intelligence and Machine Learning.",

        "Data Scientist":
        "Data Scientists analyze data and use Machine Learning "
        "techniques to generate useful insights.",

        "Web Developer":
        "Web Developers design and develop websites and "
        "web applications.",

        "Cybersecurity Analyst":
        "Cybersecurity Analysts protect computer systems, "
        "networks and data from cyber threats.",

        "Cloud Engineer":
        "Cloud Engineers manage cloud infrastructure, "
        "services and applications."
    }

    if career in career_info:

        st.info(
            career_info[career]
        )

    # --------------------------------------------------
    # OTHER CAREER POSSIBILITIES
    # --------------------------------------------------

    st.header("📊 Other Career Possibilities")

    alternatives = results.head(3).copy()

    alternatives["Confidence"] = (
        alternatives["Confidence"] * 100
    ).round(2)

    alternatives = alternatives.rename(
        columns={
            "Confidence": "Confidence (%)"
        }
    )

    st.dataframe(
        alternatives,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # STUDENT PROFILE
    # --------------------------------------------------

    st.header("📋 Student Profile")

    profile = pd.DataFrame({

        "Category": [
            "Age",
            "Degree",
            "CGPA",
            "Python",
            "Java",
            "SQL",
            "Machine Learning",
            "Communication",
            "Problem Solving",
            "Interest",
            "Projects",
            "Certifications"
        ],

        "Value": [
            age,
            degree,
            cgpa,
            python_skill,
            java_skill,
            sql_skill,
            ml_skill,
            communication,
            problem_solving,
            interest,
            projects,
            certifications
        ]
    })

    st.dataframe(
        profile,
        use_container_width=True,
        hide_index=True
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "🎓 AI-Based Career Guidance System | "
    "Python | Machine Learning | Streamlit"
)


