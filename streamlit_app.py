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

st.title('🙋🏻‍♂️ Varun Prasannan')

with open("VarunPrasannan.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download Resume",
                    data=PDFbyte,
                    file_name="VarunPrasannan.pdf",
                    mime='application/octet-stream')

st.markdown("***")

# ----------------
def redirect_button(url: str, text: str= None, color="#2076e6"):
    st.markdown(
    f"""
    <a href="{url}" target="_blank">
        <div style="
            display: inline-block;
            padding: 0.5em 7em;
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
    st.link_button('Email','mailto:vprasannan4@gmail.com', use_container_width=True)
    st.link_button('Github','https://github.com/varunprasannan', use_container_width=True)
    st.link_button('LinkedIn','https://www.linkedin.com/in/varunprasannan/', use_container_width=True)


# WORK EXPERIENCE
with st.container():
    st.title("👔 Work Experience")
    st.text(" ")
    with st.expander('AFour Technologies Pvt. Ltd.'):
        st.write("""
:blue[Project: Snowflake Accelerator (Python, Streamlit, Data Visualization)]
- Developed various functionalities with exclusive access to the company's Snowflake data files.
- Created visually engaging charts and visualizations using Matplotlib, Altair to display usage statistics.
- Transformed raw usage data into meaningful graphs, charts, and diagrams that provide users with insights
into their account's activity.\n
                 
:blue[Project: AFrosty - AI Chatbot for your databases (Python, Streamlit, Snowflake, OpenAI API, GenAI)]
- Led the Proof of Concept (PoC) with access to the company's private data and developed a chatbot which will answer questions based on your database by extracting metadata from the database such as table names,
number of columns, etc.
- This project will help developers to generate sql queries just by using natural language and will also fire the
generated query and generate results in the user interface.\n

:blue[Project: Snowflake - Google Sheets Connector (Python, Streamlit, Snowflake API)]
- Developed an application which will push data from your personal google sheet file into your Snowflake
database at regular intervals defined by the user.
- This project will enable users to use the data for various visualizations using snowflake and also secures the
data in your Google Sheet files by backing up into the Snowflake Data Warehouse.
""")

    with st.expander('Intoit Solutions Pvt. Ltd.'):
        st.write("""
- Designed and developed the company's official website, showcasing a comprehensive grasp of modern web technologies utilizing HTML, CSS, and Javascript to craft a robust foundation, ensuring an intuitive and
responsive user interface.
- Implemented dynamic features and interactive elements with React, elevating the website's functionality and
user experience.
- Employed TailwindCSS and Bootstrap to streamline the styling process, ensuring a polished and visually
appealing design.
- Collaborated closely with cross-functional teams to gather requirements and incorporate feedback, ensuring
alignment with company branding and objectives.
- Employed best practices in web design, such as responsive design principles, to guarantee optimal user
experiences across various devices.
- Engaged in continuous learning and exploration of emerging technologies, staying at the forefront of industry
trends to enhance the website's design and performance.
""")
 
    with st.expander('The Sparks Foundation'):
        st.write("• Developed a basic banking system website with various functions using Django, Python, HTML and CSS.")
        st.write("• Worked on a Data Science project based on prediction using decision tree classifier")       
        st.write("• Received a Letter of Recommendation for the same")
st.markdown("***")


#EDUCATION
with st.container():
    st.title("📚 Education")
    st.text(" ")
    st.markdown(":blue[Bachelor of Engineering] in :blue[Information Technology] from **:blue[Pimpri Chinchwad College of Engineering]**")
    st.markdown(":blue[HSC State Board] from **:blue[C.M.S English Medium High School]**")
    st.markdown(":blue[SSC State Board] from **:blue[C.M.S English Medium High School]**")
st.markdown("***")

# KEY PROJECTS
with st.container():
    st.title("🎨 Projects")
    st.text(" ")

    with st.expander('AFrosty - An AI Chatbot for your databases'):
        st.write("Developed a chatbot which can answer questions based on a particular database by automatically extracting metadata from the database such as table names, number of columns, etc. This project will help novice developers to generate sql queries just by using natural language and will also fire the generated query and generate results in the user interface.")

    with st.expander('Snowflake Accelerator'):
        st.write("Developed a Streamlit project that is a powerful tool designed to seamlessly connect with your Snowflake account, offering valuable insights and visualizations on credit usage and related metrics. With its user-friendly interface, it empowers users to efficiently monitor and optimize resource consumption, enhancing overall data management and decision-making within the Snowflake data platform.")

    with st.expander('Snowflake - Google Sheets Connector'):
        st.write("Developed a Streamlit application which will push data from your personal google sheet file into your Snowflake database at regular intervals defined by the user. This project will secure the data in your Google Sheet files by backing up into the Snowflake Data Warehouse")

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
    st.subheader("Languages")
    st.text("Python, C++, Java, SQL, HTML, CSS,  JavaScript ES6, Dart")
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

# Research Papers
with st.container():
    st.title("🔬 Research Papers")
    st.text(" ")
    with st.expander('Smart Computer Commands using Gesture Recognition - PCCDA 2023'):
        st.write("Paper available [here](https://link.springer.com/chapter/10.1007/978-981-99-4626-6_21)")
    
    with st.expander('Gesture Recognition and conversion to speech for Specially Abled - ICMISC 2022'):
        st.write("Paper available [here](https://link.springer.com/chapter/10.1007/978-981-19-6088-8_44)")
st.markdown("***")
    

# Tabs for projects mayb?
with st.container():
    st.title("📄 Certifications")
    st.text(" ")
    st.text("Responsive Web Design - freecodecamp")
    st.text("Snowflake Essentials - Data Warehousing, Data Applications, Data Sharing, Data Engineering, Data Lake")
    st.text("Python: Coursera - University Of Michigan")
    st.text("IIT Spoken Tutorial - C Programming, Git Training")
st.markdown("***")