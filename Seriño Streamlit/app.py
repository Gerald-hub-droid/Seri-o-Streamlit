
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Gerald | Personal Portfolio",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Application paths
BASE_DIR = Path(__file__).parent
PROFILE_IMAGE = BASE_DIR / "assets" / "profile.jpg"

# Student information
NAME = "Gerald Brandon Angus Seriño"
EMAIL = "serinogeraldbrandon@gmail.com"
PROGRAM = "Bachelor of Science in Mechanical Engineering"
UNIVERSITY = "North Eastern Mindanao State University - Bislig Campus"
SECTION = "BSME 2B"

# Custom styling
st.markdown("""
<style>
.stApp {
    background: #F4F6FA;
}

section[data-testid="stSidebar"] {
    background: #172B4D;
}

section[data-testid="stSidebar"] * {
    color: white;
}

section[data-testid="stSidebar"] hr {
    border-color: #52647C;
}

.block-container {
    padding-top: 2rem;
    max-width: 1400px;
}

h1, h2, h3 {
    color: #172B4D;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
}

.footer {
    text-align: center;
    color: #64748B;
    padding: 20px;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:

    st.markdown("## GERALD")
    st.caption("PERSONAL PORTFOLIO")

    st.divider()

    if PROFILE_IMAGE.exists():
        st.image(str(PROFILE_IMAGE), width=150)
    else:
        st.info("Upload your profile picture in Settings.")

    st.markdown(f"### {NAME}")
    st.caption("Mechanical Engineering Student")
    st.caption(SECTION)

    st.divider()

    st.markdown("### CONTACT")
    st.caption(EMAIL)

    st.divider()

    st.markdown("### APPLICATION")
    st.caption("Student Portfolio")
    st.caption("Version 1.0.0")

# Main page
st.title("Welcome to My Portfolio")

st.write(
    "A personal space showcasing my profile, "
    "educational background, and academic journey."
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.caption("YEAR LEVEL")
        st.subheader("2nd Year")

with col2:
    with st.container(border=True):
        st.caption("PROGRAM")
        st.subheader("BSME")

with col3:
    with st.container(border=True):
        st.caption("SECTION")
        st.subheader("BSME 2B")

st.divider()

st.header("About Me")

st.write(
    f"""
    I am **{NAME}**, currently pursuing
    **{PROGRAM}** at **{UNIVERSITY}**.

    I am a second-year student under section
    **{SECTION}**.
    """
)

st.divider()

st.header("Explore My Portfolio")

st.write(
    "Use the navigation menu in the sidebar to "
    "view my personal information, educational "
    "background, and application settings."
)

st.markdown("---")

st.markdown(
    '<div class="footer">'
    'Developed by Gerald Brandon Angus Seriño'
    '</div>',
    unsafe_allow_html=True
)
