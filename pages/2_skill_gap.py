import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Skill Gap Analysis",
    page_icon="🧩",
    layout="wide"
)

# ---------------- TITLE ----------------

st.title("🧩 Skill Gap Analysis")

st.write(
    "Analyze your current technical skills and identify areas "
    "that you can improve for different career paths."
)

st.divider()

# ---------------- SELECT CAREER ----------------

career = st.selectbox(
    "🎯 Select Your Target Career",
    [
        "AI Engineer",
        "Data Scientist",
        "Web Developer",
        "Cybersecurity Analyst",
        "Cloud Engineer"
    ]
)

st.divider()

# ---------------- SKILL REQUIREMENTS ----------------

career_skills = {

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "SQL",
        "Problem Solving"
    ],

    "Data Scientist": [
        "Python",
        "Machine Learning",
        "SQL",
        "Problem Solving"
    ],

    "Web Developer": [
        "Python",
        "Java",
        "SQL",
        "Problem Solving"
    ],

    "Cybersecurity Analyst": [
        "Python",
        "Java",
        "SQL",
        "Problem Solving"
    ],

    "Cloud Engineer": [
        "Python",
        "SQL",
        "Problem Solving",
        "Communication"
    ]
}

required_skills = career_skills[career]

# ---------------- USER SKILLS ----------------

st.subheader("💻 Your Current Skills")

python_skill = st.checkbox("Python")
java_skill = st.checkbox("Java")
sql_skill = st.checkbox("SQL")
ml_skill = st.checkbox("Machine Learning")
problem_skill = st.checkbox("Problem Solving")
communication_skill = st.checkbox("Communication")

user_skills = []

if python_skill:
    user_skills.append("Python")

if java_skill:
    user_skills.append("Java")

if sql_skill:
    user_skills.append("SQL")

if ml_skill:
    user_skills.append("Machine Learning")

if problem_skill:
    user_skills.append("Problem Solving")

if communication_skill:
    user_skills.append("Communication")

# ---------------- ANALYZE BUTTON ----------------

st.divider()

if st.button(
    "🔍 Analyze Skill Gap",
    use_container_width=True
):

    matched_skills = []

    missing_skills = []

    for skill in required_skills:

        if skill in user_skills:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    # ---------------- SCORE ----------------

    total = len(required_skills)

    completed = len(matched_skills)

    percentage = int((completed / total) * 100)

    # ---------------- RESULT ----------------

    st.subheader("📊 Skill Analysis")

    st.progress(
        percentage / 100
    )

    st.write(
        f"### Skill Readiness: {percentage}%"
    )

    # ---------------- COLUMNS ----------------

    col1, col2 = st.columns(2)

    with col1:

        st.success("✅ Skills You Have")

        if matched_skills:

            for skill in matched_skills:
                st.write(f"✔️ {skill}")

        else:

            st.write("No matching skills yet.")

    with col2:

        st.warning("⚠️ Skills To Improve")

        if missing_skills:

            for skill in missing_skills:
                st.write(f"• {skill}")

        else:

            st.write(
                "🎉 You have all the required skills!"
            )

    # ---------------- RECOMMENDATION ----------------

    st.divider()

    st.subheader("💡 Recommendation")

    if missing_skills:

        st.info(
            "Focus on developing the missing skills one by one. "
            "Building projects and completing certifications "
            "can also strengthen your career profile."
        )

    else:

        st.success(
            "Your selected skills cover the main skills "
            "listed for this career path."
        )

# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "AI-Based Career Guidance System | Skill Gap Analysis"
)
