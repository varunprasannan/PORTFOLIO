import streamlit as st

st.set_page_config(
    page_title="Varun Prasannan",
    page_icon="❄️️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This webpage is my personal online Portfolio!"
    }
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.info("🛠️ This page is still under development")
st.title('🙋🏻‍♂️ Varun Prasannan')

with open("VarunPrasannan.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download Resume",
                    data=PDFbyte,
                    file_name="VarunPrasannanResume.pdf",
                    mime='application/octet-stream')

st.markdown("***")



# ----------------
def redirect_button(url: str, text: str= None, color="#2076e6"):
    st.markdown(
    f"""
    <a href="{url}" target="_blank">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )

# ----------------
with st.sidebar:
    st.sidebar.image("Varun.jpeg")
    st.sidebar.title("Contact Info")
    redirect_button("mailto:vprasannan4@gmail.com","EMail")
    st.text(" ")
    redirect_button("https://github.com/varunprasannan","Github")
    st.text(" ")
    redirect_button("https://www.linkedin.com/in/varunprasannan/","LinkedIn")


with st.container():
    st.title("📚 Education")
    st.text(" ")
    st.markdown(":blue[B. Engg] in :blue[Information Technology] from **:blue[Pimpri Chinchwad College of Engineering]**")
    st.markdown(":blue[HSC State Board] from **:blue[C.M.S English Medium High School]**")
    st.markdown(":blue[SSC State Board] from **:blue[C.M.S English Medium High School]**")
st.markdown("***")


# WORK EXPERIENCE
with st.container():
    st.title("👔 Work Experience")
    st.text(" ")
    with st.expander('AFour Technologies Pvt. Ltd.'):
        st.write("• Created various Flask apps using Python")
        st.write("• Understood REST api concepts and development")       
        st.write("• Developed applications using Streamlit Framework for Python")

    with st.expander('Intoit Solutions Pvt. Ltd.'):
        st.write("• Part of the Web development and IT team and designed the official website")
        st.write("• Designed the official website for the company")       
 
    with st.expander('The Sparks Foundation'):
        st.write("• Developed a basic banking system website with various functions using Django, Python, HTML and CSS.")
        st.write("• Worked on a Data Science project based on prediction using decision tree classifier")       
        st.write("• Received a Letter of Recommendation for the same")
st.markdown("***")


# KEY PROJECTS
with st.container():
    st.title("🎨 Projects")
    st.text(" ")
    with st.expander('Gaming For the Specially Abled'):
        st.write("• Led a team of three and developed a game controlling mechanism with Python and OpenCV, helping the physically challenged to play games with ease.")
        st.write("• Available at this [link](https://github.com/varunprasannan/visionetic)")
    
    with st.expander('Attendance Manager'):
        st.write("• Built an attendance manager using Python and Django for online video conferencing sites (Google Meet and UpGrad) which can keep a record of the students present in the meeting and even has proxy detection for false presentee.")
        st.write("• Available at this [link](https://github.com/varunprasannan/attendancemanager)")
st.markdown("***")


# Technical Skills
with st.container():
    st.title("🧑🏻‍💻 Technical Skills")
    st.text(" ")
#     c1, c2, c3 = st.columns(3)
#     with c1:
#         st.subheader("Languages")
#         st.write('Python')
#         st.write('SQL')
#         st.write('C++')
#         st.write('Java')
#         st.write('HTML')
#         st.write('CSS')
#         #st.write('Dart')
#     with c2:
#         st.subheader("Skills")
#         st.write('Git')
#         st.write('Linux')
#         st.write('POSIX')
#         st.write('Snowflake')
#         st.write('Docker')
#         st.write('MongoDB')
#     with c3:
#         st.subheader("Frameworks")
#         st.write('Streamlit')
#         st.write('Flask (REST)')
#         st.write('Django')
#         st.write('OpenCV')
# st.markdown("***")
    st.subheader("Languages")
    st.text("Python, C++, Java, SQL, HTML, CSS,  JavaScript, Dart")
    st.text(" ")
    st.text(" ")
    st.subheader("Skills")
    st.text("Git, Snowflake, Linux, Docker, MongoDB, Flutter, Verbal and Written communication skills, Clean Code Practices")
    st.text(" ")
    st.text(" ")
    st.subheader("Frameworks")
    st.text("Flask(REST), Django, Streamlit, React.js, Node.js")
    st.text(" ")
    st.markdown("***")

with st.container():
    st.title("📄 Research Papers")
    st.text(" ")
    with st.expander('Smart Computer Commands using Gesture Recognition - PCCDA 2023'):
        st.write("Paper available [here](https://link.springer.com/chapter/10.1007/978-981-19-6088-8_44)")
    
    with st.expander('Gesture Recognition and conversion to speech for Specially Abled - ICMISC 2022'):
        st.write("Paper available [here](https://link.springer.com/chapter/10.1007/978-981-19-6088-8_44)")
st.markdown("***")
    

# Tabs for projects mayb?