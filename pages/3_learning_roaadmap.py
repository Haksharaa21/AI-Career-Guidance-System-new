import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Learning Roadmap",
    page_icon="🗺️",
    layout="wide"
)

# ---------------- TITLE ----------------

st.title("🗺️ Career Learning Roadmap")

st.write(
    "Follow a structured learning path to develop the skills "
    "required for your selected career."
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

# ---------------- ROADMAP DATA ----------------

roadmaps = {

    "AI Engineer": [
        ("Step 1", "Python Programming",
         "Learn Python basics, functions, OOP and file handling."),

        ("Step 2", "NumPy and Pandas",
         "Learn data manipulation and numerical computing."),

        ("Step 3", "Data Visualization",
         "Learn Matplotlib and create meaningful visualizations."),

        ("Step 4", "Machine Learning",
         "Learn regression, classification and clustering."),

        ("Step 5", "Deep Learning",
         "Learn neural networks and deep learning concepts."),

        ("Step 6", "AI Projects",
         "Build practical AI projects and deploy them.")
    ],

    "Data Scientist": [
        ("Step 1", "Python",
         "Learn Python programming and data handling."),

        ("Step 2", "Statistics",
         "Learn basic statistics and probability."),

        ("Step 3", "Pandas and NumPy",
         "Learn data cleaning and analysis."),

        ("Step 4", "Data Visualization",
         "Learn charts and visualization techniques."),

        ("Step 5", "Machine Learning",
         "Learn supervised and unsupervised learning."),

        ("Step 6", "Data Science Projects",
         "Build projects using real-world datasets.")
    ],

    "Web Developer": [
        ("Step 1", "HTML",
         "Learn the structure of web pages."),

        ("Step 2", "CSS",
         "Learn styling, layouts and responsive design."),

        ("Step 3", "JavaScript",
         "Learn programming for interactive websites."),

        ("Step 4", "Frontend Frameworks",
         "Learn modern frontend development concepts."),

        ("Step 5", "Backend Development",
         "Learn server-side programming and databases."),

        ("Step 6", "Web Projects",
         "Build and deploy complete web applications.")
    ],

    "Cybersecurity Analyst": [
        ("Step 1", "Networking",
         "Learn IP addresses, protocols, ports and network concepts."),

        ("Step 2", "Linux",
         "Learn Linux commands and system administration."),

        ("Step 3", "Cybersecurity Basics",
         "Learn threats, vulnerabilities and security principles."),

        ("Step 4", "Security Tools",
         "Learn tools used for network and security analysis."),

        ("Step 5", "Ethical Hacking",
         "Learn penetration testing concepts in authorized environments."),

        ("Step 6", "Security Projects",
         "Build practical cybersecurity projects and labs.")
    ],

    "Cloud Engineer": [
        ("Step 1", "Networking",
         "Learn networking fundamentals and protocols."),

        ("Step 2", "Linux",
         "Learn Linux administration and command-line tools."),

        ("Step 3", "Cloud Fundamentals",
         "Learn cloud computing concepts and services."),

        ("Step 4", "Cloud Platform",
         "Learn services offered by a major cloud platform."),

        ("Step 5", "DevOps",
         "Learn deployment, automation and CI/CD concepts."),

        ("Step 6", "Cloud Projects",
         "Build and deploy cloud-based applications.")
    ]
}

# ---------------- DISPLAY ROADMAP ----------------

st.subheader(f"🚀 Roadmap for {career}")

roadmap = roadmaps[career]

for step, title, description in roadmap:

    with st.container(border=True):

        st.markdown(f"### {step} — {title}")

        st.write(description)

# ---------------- FINAL MESSAGE ----------------

st.divider()

st.success(
    "💡 Tip: Learn one step at a time and build a small project "
    "after completing each major skill."
)

# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "AI-Based Career Guidance System | Learning Roadmap"
)
