import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Career Comparison",
    page_icon="🔄",
    layout="wide"
)

# ---------------- TITLE ----------------

st.title("🔄 Career Comparison")

st.write(
    "Compare two career paths based on skills, learning areas "
    "and project requirements."
)

st.divider()

# ---------------- CAREER DATA ----------------

career_data = {

    "AI Engineer": {
        "skills": [
            "Python",
            "Machine Learning",
            "SQL",
            "Problem Solving"
        ],
        "learning": [
            "Python",
            "Data Science",
            "Machine Learning",
            "Deep Learning"
        ],
        "projects": [
            "AI Chatbot",
            "Recommendation System",
            "Machine Learning Application"
        ]
    },

    "Data Scientist": {
        "skills": [
            "Python",
            "Machine Learning",
            "SQL",
            "Problem Solving"
        ],
        "learning": [
            "Python",
            "Statistics",
            "Data Analysis",
            "Machine Learning"
        ],
        "projects": [
            "Sales Prediction",
            "Customer Analysis",
            "Data Analytics Dashboard"
        ]
    },

    "Web Developer": {
        "skills": [
            "Python",
            "Java",
            "SQL",
            "Problem Solving"
        ],
        "learning": [
            "HTML",
            "CSS",
            "JavaScript",
            "Backend Development"
        ],
        "projects": [
            "Portfolio Website",
            "E-Commerce Website",
            "Web Application"
        ]
    },

    "Cybersecurity Analyst": {
        "skills": [
            "Python",
            "Java",
            "SQL",
            "Problem Solving"
        ],
        "learning": [
            "Networking",
            "Linux",
            "Cybersecurity",
            "Security Tools"
        ],
        "projects": [
            "Network Monitoring",
            "Security Analysis",
            "Digital Forensics"
        ]
    },

    "Cloud Engineer": {
        "skills": [
            "Python",
            "SQL",
            "Problem Solving",
            "Communication"
        ],
        "learning": [
            "Networking",
            "Linux",
            "Cloud Computing",
            "DevOps"
        ],
        "projects": [
            "Cloud Deployment",
            "Cloud Storage System",
            "CI/CD Pipeline"
        ]
    }
}

# ---------------- CAREER SELECTION ----------------

col1, col2 = st.columns(2)

with col1:

    career1 = st.selectbox(
        "🎯 Select First Career",
        list(career_data.keys()),
        index=0
    )

with col2:

    career2 = st.selectbox(
        "🎯 Select Second Career",
        list(career_data.keys()),
        index=1
    )

st.divider()

# ---------------- COMPARISON ----------------

data1 = career_data[career1]
data2 = career_data[career2]

col1, col2 = st.columns(2)

# ---------------- FIRST CAREER ----------------

with col1:

    st.header(f"💼 {career1}")

    st.subheader("💻 Important Skills")

    for skill in data1["skills"]:
        st.write(f"✔️ {skill}")

    st.subheader("📚 Learning Areas")

    for item in data1["learning"]:
        st.write(f"📖 {item}")

    st.subheader("🛠️ Project Ideas")

    for project in data1["projects"]:
        st.write(f"🔹 {project}")

# ---------------- SECOND CAREER ----------------

with col2:

    st.header(f"💼 {career2}")

    st.subheader("💻 Important Skills")

    for skill in data2["skills"]:
        st.write(f"✔️ {skill}")

    st.subheader("📚 Learning Areas")

    for item in data2["learning"]:
        st.write(f"📖 {item}")

    st.subheader("🛠️ Project Ideas")

    for project in data2["projects"]:
        st.write(f"🔹 {project}")

# ---------------- COMMON SKILLS ----------------

st.divider()

st.subheader("🔗 Common Skills")

common_skills = set(data1["skills"]).intersection(
    set(data2["skills"])
)

if common_skills:

    for skill in common_skills:
        st.write(f"✔️ {skill}")

else:

    st.write("No common skills listed.")

# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "AI-Based Career Guidance System | Career Comparison"
)
