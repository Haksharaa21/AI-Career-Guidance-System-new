import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Course Recommendations",
    page_icon="📚",
    layout="wide"
)

# ---------------- TITLE ----------------

st.title("📚 Course Recommendations")

st.write(
    "Explore recommended learning topics and resources "
    "based on your selected career."
)

st.divider()

# ---------------- CAREER SELECTION ----------------

career = st.selectbox(
    "🎯 Select Your Career",
    [
        "AI Engineer",
        "Data Scientist",
        "Web Developer",
        "Cybersecurity Analyst",
        "Cloud Engineer"
    ]
)

# ---------------- COURSE DATA ----------------

courses = {

    "AI Engineer": [
        ("Python Programming", "Beginner", "Learn Python fundamentals and programming concepts."),
        ("NumPy & Pandas", "Beginner", "Learn numerical computing and data manipulation."),
        ("Machine Learning", "Intermediate", "Learn classification, regression and clustering."),
        ("Deep Learning", "Advanced", "Learn neural networks and deep learning."),
        ("Artificial Intelligence", "Advanced", "Learn important AI concepts and applications.")
    ],

    "Data Scientist": [
        ("Python for Data Science", "Beginner", "Learn Python for data analysis."),
        ("Statistics", "Beginner", "Learn probability and statistical concepts."),
        ("Pandas & NumPy", "Beginner", "Learn data cleaning and analysis."),
        ("Machine Learning", "Intermediate", "Learn predictive modelling techniques."),
        ("Data Visualization", "Intermediate", "Learn how to communicate insights using charts.")
    ],

    "Web Developer": [
        ("HTML", "Beginner", "Learn the structure of web pages."),
        ("CSS", "Beginner", "Learn styling and responsive layouts."),
        ("JavaScript", "Intermediate", "Create interactive web applications."),
        ("Frontend Development", "Intermediate", "Learn modern frontend development."),
        ("Backend Development", "Advanced", "Learn servers, APIs and databases.")
    ],

    "Cybersecurity Analyst": [
        ("Computer Networks", "Beginner", "Learn networking fundamentals."),
        ("Linux", "Beginner", "Learn Linux commands and system administration."),
        ("Cybersecurity Fundamentals", "Beginner", "Understand common security threats."),
        ("Ethical Hacking", "Intermediate", "Learn authorized security testing concepts."),
        ("Network Security", "Advanced", "Learn methods for protecting networks.")
    ],

    "Cloud Engineer": [
        ("Networking Fundamentals", "Beginner", "Learn networks and communication protocols."),
        ("Linux Administration", "Beginner", "Learn Linux system administration."),
        ("Cloud Computing", "Beginner", "Understand cloud concepts and services."),
        ("Cloud Architecture", "Intermediate", "Learn how cloud systems are designed."),
        ("DevOps", "Advanced", "Learn automation, deployment and CI/CD.")
    ]
}

# ---------------- DISPLAY COURSES ----------------

st.subheader(f"🎓 Recommended Learning Path for {career}")

for course, level, description in courses[career]:

    with st.container(border=True):

        st.markdown(f"### 📖 {course}")

        st.write(f"**Level:** {level}")

        st.write(description)

# ---------------- TIP ----------------

st.divider()

st.info(
    "💡 Tip: Complete the beginner topics first, then gradually "
    "move to intermediate and advanced topics."
)

# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "AI-Based Career Guidance System | Course Recommendations"
)
