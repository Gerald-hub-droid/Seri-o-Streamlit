import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Gerald's Personal Profile",
    page_icon="👤",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>
.profile-title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
}
.profile-subtitle {
    text-align: center;
    color: gray;
}
.section-title {
    color: #3498db;
    font-size: 24px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR PROFILE
with st.sidebar:
    st.image("profile.jpg", width=180)

    st.markdown("## Gerald Brandon Angus Seriño")
    st.caption("BSME 2B Student")

    st.divider()

    st.markdown("### Navigation")

    page = st.radio(
        "Select a page:",
        ["Home", "Personal Information",
         "Educational Background"]
    )

# HOME PAGE
if page == "Home":

    st.markdown(
        '<div class="profile-title">'
        'Gerald Brandon Angus Seriño</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="profile-subtitle">'
        'Bachelor of Science in Mechanical Engineering'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(" ")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🎓 **2nd Year Student**")

    with col2:
        st.info("📚 **BSME 2B**")

    with col3:
        st.info("🏫 **NEMSU - Bislig**")

    st.divider()

    st.markdown("### Welcome to My Personal Profile!")

    st.write("""
    Hello! My name is Gerald Brandon Angus Seriño.
    I am currently a second-year Bachelor of Science
    in Mechanical Engineering student at North Eastern
    Mindanao State University - Bislig Campus.

    This website contains my personal information
    and educational background.
    """)

# PERSONAL INFORMATION
elif page == "Personal Information":

    st.title("Personal Information")

    st.divider()

    st.write("**Full Name:** Gerald Brandon Angus Seriño")

    st.write("**Email Address:** serinogeraldbrandon@gmail.com")

    st.write("**Birthday:** August 09, 2007")

    st.write("**Age:** 19")

    st.write("**Program:** Bachelor of Science in Mechanical Engineering")

    st.write("**University:** North Eastern Mindanao State University - Bislig Campus")

    st.write("**Year Level:** 2nd Year")

    st.write("**Section:** BSME 2B")

# EDUCATIONAL BACKGROUND
elif page == "Educational Background":

    st.title("Educational Background")

    st.write(
        "Here is a summary of my academic journey."
    )

    st.divider()

    education = [
        (
            "Elementary Education",
            "Mangagoy Hilltop Elementary School",
            "2013 - 2019"
        ),
        (
            "Junior High School",
            "Tabon Maximino Estrella National High School",
            "2019 - 2023"
        ),
        (
            "Senior High School",
            "Tabon Maximino Estrella National High School",
            "2023 - 2025"
        ),
        (
            "College Education",
            "North Eastern Mindanao State University - Bislig Campus",
            "2025 - Present"
        )
    ]

    for level, school, year in education:

        with st.container(border=True):

            st.subheader(level)

            st.write("🏫 **School:**", school)

            st.write("📅 **School Year:**", year)

    st.divider()

    st.success(
        "Currently pursuing Bachelor of Science "
        "in Mechanical Engineering - 2nd Year (BSME 2B)"
    )

# FOOTER
st.divider()

st.caption(
    "© 2026 Gerald Brandon Angus Seriño | Personal Profile"
)
