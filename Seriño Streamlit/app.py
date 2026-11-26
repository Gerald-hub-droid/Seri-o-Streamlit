
import streamlit as st
from PIL import Image
from pathlib import Path

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Gerald Brandon Angus Seriño",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: #f4f6fa;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1150px;
}

.hero {
    background: linear-gradient(135deg, #0f172a, #172554, #334155);
    padding: 65px 30px;
    border-radius: 25px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 38px;
    font-weight: 800;
    color: white;
}

.hero p {
    color: #cbd5e1;
    font-size: 15px;
}

.section-title {
    color: #172554;
    font-weight: 700;
    font-size: 28px;
    margin-bottom: 15px;
}

.profile-card {
    background: white;
    border-radius: 18px;
    padding: 25px;
    border: 1px solid #e2e8f0;
    margin-bottom: 15px;
}

.info-label {
    color: #64748b;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
}

.info-value {
    color: #172554;
    font-size: 15px;
    font-weight: 600;
}

.timeline {
    border-left: 3px solid #334155;
    padding: 5px 0 5px 22px;
    margin: 15px 0;
}

.timeline h4 {
    color: #172554;
    margin-bottom: 5px;
}

.timeline p {
    color: #64748b;
    font-size: 14px;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    padding: 25px 0;
}

.stButton > button {
    border-radius: 12px;
    font-weight: 600;
    min-height: 45px;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# SESSION STATE
# ==========================================

if "started" not in st.session_state:
    st.session_state.started = False

if "page" not in st.session_state:
    st.session_state.page = "Home"

# ==========================================
# PERSONAL INFORMATION
# ==========================================

NAME = "Gerald Brandon Angus Seriño"

EMAIL = "serinogeraldbrandon@gmail.com"
ALT_EMAIL = "sgeraldbrandon@gmail.com"

PHONE = "09976908659"

UNIVERSITY = "North Eastern Mindanao State University"
CAMPUS = "Bislig Campus"
COURSE = "Bachelor of Science in Mechanical Engineering"
YEAR_LEVEL = "Sophomore (2nd Year)"
SECTION = "BSME-2B"


# ==========================================
# WELCOME SCREEN
# ==========================================

def welcome_screen():

    st.markdown("""
    <div class="hero">
        <h1>WELCOME</h1>
        <p>Discover my profile, academic journey, and personal introduction.</p>
        <br>
        <h2>Gerald Brandon Angus Seriño</h2>
        <p>Aspiring Mechanical Engineer | Student | Future Innovator</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button("🚀 GET STARTED", use_container_width=True):
            st.session_state.started = True
            st.rerun()

    st.markdown("""
    <div class="footer">
        Designed and Developed by Gerald Brandon Angus Seriño<br>
        © 2026 All Rights Reserved
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# NAVIGATION
# ==========================================

def navigation():

    st.sidebar.title("⚙️ The Engineer's Hub")
    st.sidebar.caption("PERSONAL APPLICATION")
    st.sidebar.divider()

    pages = [
        "Home",
        "About Me",
        "Educational Background",
        "Developer Profile"
    ]

    for page in pages:
        if st.sidebar.button(page, use_container_width=True):
            st.session_state.page = page
            st.rerun()

    st.sidebar.divider()

    if st.sidebar.button("Logout / Welcome Screen",
                         use_container_width=True):
        st.session_state.started = False
        st.session_state.page = "Home"
        st.rerun()


# ==========================================
# HOME PAGE
# ==========================================

def home_page():

    st.markdown("""
    <div class="hero">
        <h1>Hello, Welcome!</h1>
        <h2>I'm Gerald Brandon Angus Seriño</h2>
        <p>Welcome to my personal application.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Dashboard</div>',
                unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Year Level", "2nd Year")
    col2.metric("Program", "BSME")
    col3.metric("Section", "BSME-2B")

    st.markdown("---")

    st.subheader("About This Application")

    st.write("""
    This application serves as my personal digital profile,
    showcasing my personal introduction, educational background,
    academic journey, and developer information.

    Explore the different sections using the navigation menu.
    """)


# ==========================================
# ABOUT ME
# ==========================================

def about_page():

    st.markdown('<div class="section-title">About Me</div>',
                unsafe_allow_html=True)

    st.markdown(f"""
    <div class="profile-card">
        <h2 style="color:#172554;">{NAME}</h2>
        <p style="color:#64748b;">
        Aspiring Mechanical Engineer | Technology Enthusiast
        </p>
        <hr>
        <p style="color:#334155; line-height:1.9;">
        Hello! My name is <b>{NAME}</b>. I am currently a sophomore
        student pursuing a Bachelor of Science in Mechanical
        Engineering at North Eastern Mindanao State University
        (NEMSU) - Bislig Campus.
        <br><br>
        My academic journey includes elementary education,
        the Special Program in the Arts (SPA) - Media Arts section
        during junior high school, and the Science, Technology,
        Engineering, and Mathematics (STEM) strand during senior
        high school.
        <br><br>
        I am interested in creativity, technology, engineering,
        innovation, and application development. I enjoy learning
        new things and exploring ideas that can help me grow
        academically and personally.
        <br><br>
        My goal is to continuously improve my knowledge and
        abilities while creating meaningful and practical solutions.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# EDUCATIONAL BACKGROUND
# ==========================================

def education_page():

    st.markdown(
        '<div class="section-title">Educational Background</div>',
        unsafe_allow_html=True
    )

    education = [
        {
            "level": "Elementary Education",
            "school": "Mangagoy Hilltop Elementary School",
            "years": "2013–2019",
            "details": "Elementary Graduate"
        },
        {
            "level": "Junior High School",
            "school": "Tabon Maximino Estrella National High School (TMENHS)",
            "years": "2019–2023",
            "details": "Section: Special Program in the Arts (SPA) – Media Arts"
        },
        {
            "level": "Senior High School",
            "school": "Tabon Maximino Estrella National High School (TMENHS)",
            "years": "2023–2025",
            "details": "Strand: Science, Technology, Engineering, and Mathematics (STEM)"
        },
        {
            "level": "College Education",
            "school": "North Eastern Mindanao State University (NEMSU) – Bislig Campus",
            "years": "2025–Present",
            "details": "Bachelor of Science in Mechanical Engineering | Sophomore | BSME-2B"
        }
    ]

    for item in education:
        st.markdown(f"""
        <div class="profile-card">
            <div class="info-label">{item['years']}</div>
            <h3 style="color:#172554;">{item['level']}</h3>
            <p style="color:#334155;font-weight:600;">
                {item['school']}
            </p>
            <p style="color:#64748b;">
                {item['details']}
            </p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# DEVELOPER PROFILE
# ==========================================

def developer_page():

    st.markdown(
        '<div class="section-title">Developer Profile</div>',
        unsafe_allow_html=True
    )

    # Profile Picture and Name
    col1, col2 = st.columns([1, 3])

    with col1:
        profile_path = Path(__file__).parent / "profile.jpg"

        if profile_path.exists():
            image = Image.open(profile_path)
            st.image(image, width=180)
        else:
            st.warning("Profile picture not found.")

    with col2:
        st.markdown(
            f"<h2 style='color:#172554;'>{NAME}</h2>",
            unsafe_allow_html=True
        )
        st.caption("Application Owner and Developer")
        st.write("Aspiring Mechanical Engineer | Technology Enthusiast")

    st.divider()

    # Academic Information
    with st.container(border=True):

        st.subheader("Academic Information")

        st.markdown("**UNIVERSITY**")
        st.write(UNIVERSITY)

        st.markdown("**CAMPUS**")
        st.write(CAMPUS)

        st.markdown("**PROGRAM**")
        st.write(COURSE)

        st.markdown("**YEAR LEVEL**")
        st.write(YEAR_LEVEL)

        st.markdown("**SECTION**")
        st.write(SECTION)

    # Contact Information
    st.subheader("Contact Information")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**📧 Primary Email**")
        st.write(EMAIL)

        st.markdown("**📱 Contact Number**")
        st.write(PHONE)

    with col2:
        st.markdown("**📧 Alternative Email**")
        st.write(ALT_EMAIL)

# ==========================================
# MAIN APPLICATION
# ==========================================

if not st.session_state.started:

    welcome_screen()

else:

    navigation()

    if st.session_state.page == "Home":
        home_page()

    elif st.session_state.page == "About Me":
        about_page()

    elif st.session_state.page == "Educational Background":
        education_page()

    elif st.session_state.page == "Developer Profile":
        developer_page()

    st.markdown("""
    <div class="footer">
        Developed by Gerald Brandon Angus Seriño<br>
        © 2026 All Rights Reserved
    </div>
    """, unsafe_allow_html=True)
