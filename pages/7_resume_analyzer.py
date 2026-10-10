import streamlit as st

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write(
    "Upload your resume and check your skills against different career paths."
)

st.divider()

# Career skill requirements
career_skills = {
    "AI Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "sql",
        "tensorflow",
        "pytorch"
    ],

    "Data Scientist": [
        "python",
        "sql",
        "machine learning",
        "statistics",
        "pandas",
        "data analysis"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "python",
        "react",
        "sql"
    ],

    "Cybersecurity Analyst": [
        "networking",
        "linux",
        "cybersecurity",
        "ethical hacking",
        "python",
        "wireshark"
    ],

    "Cloud Engineer": [
        "cloud computing",
        "linux",
        "networking",
        "aws",
        "azure",
        "docker"
    ]
}

# Resume upload
uploaded_file = st.file_uploader(
    "📤 Upload your resume (.txt file)",
    type=["txt"]
)

if uploaded_file is not None:

    resume_text = uploaded_file.read().decode(
        "utf-8",
        errors="ignore"
    ).lower()

    st.success("Resume uploaded successfully!")

    st.header("🔍 Resume Analysis")

    # Find skills
    found_skills = []

    all_skills = set()

    for skills in career_skills.values():
        for skill in skills:
            all_skills.add(skill)

    for skill in all_skills:
        if skill in resume_text:
            found_skills.append(skill)

    # Display found skills
    st.subheader("✅ Skills Found in Resume")

    if found_skills:
        for skill in sorted(found_skills):
            st.write("•", skill.title())
    else:
        st.warning("No matching technical skills were detected.")

    st.divider()

    # Career matching
    st.subheader("🎯 Career Skill Matching")

    career_results = []

    for career, skills in career_skills.items():

        matched = []

        for skill in skills:
            if skill in resume_text:
                matched.append(skill)

        percentage = (len(matched) / len(skills)) * 100

        career_results.append({
            "Career": career,
            "Matched Skills": len(matched),
            "Required Skills": len(skills),
            "Match Percentage": round(percentage, 2)
        })

    # Sort results
    career_results = sorted(
        career_results,
        key=lambda x: x["Match Percentage"],
        reverse=True
    )

    # Display table
    st.dataframe(
        career_results,
        use_container_width=True,
        hide_index=True
    )

    # Career suggestions
    st.subheader("💡 Career Suggestions")

    for result in career_results[:3]:

        career = result["Career"]
        percentage = result["Match Percentage"]

        st.write(
            f"**{career} — {percentage}% skill match**"
        )

    st.divider()

    # Missing skills
    st.subheader("📚 Skills You Can Improve")

    selected_career = st.selectbox(
        "Select a career to view missing skills",
        list(career_skills.keys())
    )

    missing_skills = []

    for skill in career_skills[selected_career]:

        if skill not in resume_text:
            missing_skills.append(skill)

    if missing_skills:

        for skill in missing_skills:
            st.write("❌", skill.title())

    else:
        st.success(
            "All listed skills for this career were found in your resume!"
        )

    st.divider()

    st.info(
        "This analyzer checks for keywords in the uploaded resume. "
        "The match percentage is a simple skill-match indicator and "
        "does not represent actual hiring probability."
    )

else:

    st.info(
        "Please upload a .txt resume file to start the analysis."
    )

st.divider()

st.caption(
    "AI Career Guidance System | Resume Analyzer | Python | Streamlit"
)
