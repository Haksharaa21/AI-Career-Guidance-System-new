import streamlit as st

st.set_page_config(
    page_title="AI Career Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career Guidance Chatbot")
st.write("Ask questions about careers, skills, learning and projects.")

st.divider()

# Career information
career_data = {
    "AI Engineer": {
        "skills": "Python, Machine Learning, Deep Learning, Mathematics and SQL",
        "learning": "Python → Machine Learning → Deep Learning → AI Projects",
        "projects": "Chatbot, Recommendation System, Image Classification"
    },

    "Data Scientist": {
        "skills": "Python, SQL, Statistics, Data Analysis and Machine Learning",
        "learning": "Python → Pandas → Statistics → Machine Learning → Data Projects",
        "projects": "Sales Prediction, Student Analysis, Customer Segmentation"
    },

    "Web Developer": {
        "skills": "HTML, CSS, JavaScript, Frontend and Backend Development",
        "learning": "HTML → CSS → JavaScript → Backend → Database",
        "projects": "Portfolio Website, E-commerce Website, Student Management System"
    },

    "Cybersecurity Analyst": {
        "skills": "Networking, Linux, Cybersecurity, Ethical Hacking and Security Tools",
        "learning": "Networking → Linux → Security Basics → Ethical Hacking",
        "projects": "Network Scanner, Password Strength Checker, Security Monitoring"
    },

    "Cloud Engineer": {
        "skills": "Cloud Computing, Linux, Networking, Virtualization and Cloud Platforms",
        "learning": "Networking → Linux → Cloud Basics → Cloud Services",
        "projects": "Cloud Storage System, Cloud Monitoring Dashboard, Web Deployment"
    }
}

# User question
question = st.text_input(
    "💬 Ask your career question",
    placeholder="Example: What skills are needed for AI Engineer?"
)

if st.button("🤖 Ask Chatbot", use_container_width=True):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:
        q = question.lower()

        found_career = None

        for career in career_data:
            if career.lower() in q:
                found_career = career
                break

        # Career-specific questions
        if found_career:

            data = career_data[found_career]

            st.success(f"Career: {found_career}")

            if "skill" in q:
                st.write("### 🛠️ Required Skills")
                st.info(data["skills"])

            elif "learn" in q or "roadmap" in q:
                st.write("### 📚 Learning Path")
                st.info(data["learning"])

            elif "project" in q:
                st.write("### 💡 Project Ideas")
                st.info(data["projects"])

            else:
                st.write("### 🎯 Career Information")
                st.info(
                    f"**Skills:** {data['skills']}\n\n"
                    f"**Learning Path:** {data['learning']}\n\n"
                    f"**Project Ideas:** {data['projects']}"
                )

        # General questions
        elif "career" in q and "choose" in q:
            st.info(
                "You can choose a career based on your interests, "
                "skills, academic background and career goals."
            )

        elif "skill" in q:
            st.info(
                "Important technical skills include Python, SQL, "
                "Machine Learning, Web Development, Networking and Cloud Computing."
            )

        elif "project" in q:
            st.info(
                "Projects help demonstrate practical knowledge. "
                "Choose projects related to your target career."
            )

        elif "python" in q:
            st.info(
                "Python is widely used in AI, Data Science, "
                "Web Development and Automation."
            )

        else:
            st.info(
                "I can help you with career skills, learning paths, "
                "project ideas and career information."
            )

st.divider()

st.subheader("💡 Example Questions")

st.write("• What skills are needed for AI Engineer?")
st.write("• What should I learn for Data Scientist?")
st.write("• Give me project ideas for Web Developer")
st.write("• What skills are needed for Cybersecurity Analyst?")
st.write("• What is the learning roadmap for Cloud Engineer?")

st.divider()

st.caption(
    "AI Career Guidance System | Career Chatbot | Python | Streamlit"
)
