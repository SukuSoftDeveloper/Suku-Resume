from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | John Doe"
PAGE_ICON = ":wave:"
NAME = "Sudheer Kumar"
DESCRIPTION = """
Associate Software Engineer, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "Sudheerannameti0406@e=gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Web Applications - Works with Rest API's and Performed Authentication & Authorization": "https://youtu.be/Sb0A9i6d320",
    "🏆 Library Management System - Can store all books and assign books, Renew Books in the librarry etc.": "https://youtu.be/3egaMfE9388",
    "🏆 Bug Tracking System - Can track the bugs raised by team members and fix it in short time": "https://youtu.be/LzCfNanQ_9c",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 2.3 Years expereince developing web applications
- ✔️ Strong hands on experience and knowledge in C# , Python, Asp.Net Mvc and SQL.
- ✔️ Good understanding of solid principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming:C#, Asp.Net MVC, .Net Core and Web API
- 📊 Tools: Visual Studio & Code , MS Sql Server and Github
- 🗄️ Databases: MS Access , MS Sqlserver
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Associate Software Engineer | Mphasis Ltd**")
st.write("04/2022 - Present")
st.write(
    """
- ► Used C# , Asp.Net Mvc and SQL to create robust web based applications
- ► Compiled, studied, and inferred large amounts of data,
- ► Performed Unit Testing on applications and done POC's on the applications
- ► Good knowledge creating Web API's with robust security and Implementation
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Trainee Associate Software Engineer | Mphasis Ltd**")
st.write("01/2022 - 04/2022")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
