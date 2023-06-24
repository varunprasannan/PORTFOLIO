import streamlit as st
from st_functions import st_button, load_css
load_css()

st.set_page_config(
    page_title="Varun Prasannan",
    page_icon="❄️️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This webpage is my personal online Portfolio!"
    }
)
st.title('Varun Prasannan')

with open("VarunPrasannan.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download Resume",
                    data=PDFbyte,
                    file_name="VarunPrasannanResume.pdf",
                    mime='application/octet-stream')

st.markdown("***")
icon_size = 20
st.sidebar.image("Varun.jpeg")
st.sidebar.title("Contact Info")
st_button('linkedin', 'https://www.linkedin.com/in/varunprasannan/', 'Follow me on LinkedIn', icon_size)
st_button('github', 'https://github.com/varunprasannan/', 'Check out my Github profile', icon_size)

# with st.sidebar:
#     st.header("Contact Info")
#     st.button("[Github](https://github.com/varunprasannan)")
#     st.button("[LinkedIn](https://github.com/varunprasannan)")

with st.container():
    st.title("📚 Education")
    st.markdown(":blue[B. Engg] in :blue[Information Technology] from **:blue[Pimpri Chinchwad College of Engineering]**")
    st.markdown(":blue[HSC State Board] from **:blue[C.M.S English Medium High School]**")
    st.markdown(":blue[SSC State Board] from **:blue[C.M.S English Medium High School]**")
st.markdown("***")

# WORK EXPERIENCE
with st.container():
    st.title("🧑🏻‍💻 Work Experience")
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
    with st.expander('Gaming For the Specially Abled'):
        st.write("• Led a team of three and developed a game controlling mechanism with Python and OpenCV, helping the physically challenged to play games with ease.")
        st.write("• Available at this [link](https://github.com/varunprasannan/visionetic)")
    
    with st.expander('Attendance Manager'):
        st.write("• Built an attendance manager using Python and Django for online video conferencing sites (Google Meet and UpGrad) which can keep a record of the students present in the meeting and even has proxy detection for false presentee.")
        st.write("• Available at this [link](https://github.com/varunprasannan/attendancemanager)")
st.markdown("***")

with st.container():
    st.title("Technical Skills")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("Languages")
        st.write('Python')
        st.write('SQL')
        st.write('C++')
        st.write('Java')
        st.write('HTML')
        st.write('CSS')
        #st.write('Dart')
    with c2:
        st.subheader("Skills")
        st.write('Git')
        st.write('Linux')
        st.write('POSIX')
        st.write('Snowflake')
        st.write('Docker')
        st.write('MongoDB')
    with c3:
        st.subheader("Frameworks")
        st.write('Streamlit')
        st.write('Flask (REST)')
        st.write('Django')
        st.write('OpenCV')
st.markdown("***")


# Tabs for projects mayb?