import streamlit as st

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Gerald | Student Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# PERSONAL INFORMATION
# =====================================

NAME = "Gerald Brandon Angus Seriño"
EMAIL = "serinogeraldbrandon@gmail.com"
BIRTHDAY = "August 09, 2007"
PROGRAM = "Bachelor of Science in Mechanical Engineering"
UNIVERSITY = "North Eastern Mindanao State University - Bislig Campus"
YEAR_LEVEL = "2nd Year"
SECTION = "BSME 2B"

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #F4F6FA;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #172B4D;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white;
}

/* Sidebar divider */
section[data-testid="stSidebar"] hr {
    border-color: #52647C;
}

/* Main headings */
h1, h2, h3 {
    color: #172B4D;
}

/* Profile picture */
div[data-testid="stImage"] img {
    border-radius: 15px;
}

/* Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: white;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
}

/* Buttons */
.stButton button {
    border-radius: 8px;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748B;
    font-size: 13px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.markdown("## 🎓 MY PORTFOLIO")
    st.caption("STUDENT PERSONAL WEBSITE")

    st.divider()

    # Profile picture
    try:
        st.image("profile.jpg", width=180)
    except Exception:
        st.warning("Please add your profile.jpg file.")

    st.markdown(f"### {NAME}")
    st.caption("Mechanical Engineering Student")

    st.success("● Currently Enrolled")

    st.divider()

    # Contact information
    st.markdown("### 📌 CONTACT")
    st.caption("EMAIL ADDRESS")
    st.write(EMAIL)

    st.divider()

    # Navigation
    st.markdown("### 🧭 NAVIGATION")

    page = st.radio(
        "Choose a page:",
        [
            "Home",
            "My Profile",
            "Educational Background"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.caption("NEMSU - BISLIG CAMPUS")
    st.caption("© 2026 Gerald Seriño")


# =====================================
# HOME PAGE
# =====================================

if page == "Home":

    st.title("Welcome to My Portfolio 👋")

    st.markdown(
        "### Hello! I'm Gerald Brandon Angus Seriño."
    )

    st.write(
        "Welcome to my personal student portfolio! "
        "This website introduces who I am, my personal "
        "information, and my educational journey."
    )

    st.divider()

    # Dashboard cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Year Level", "2nd Year")

    with col2:
        st.metric("Program", "BSME")

    with col3:
        st.metric("Section", "BSME 2B")

    st.divider()

    st.subheader("👨‍🎓 About Me")

    st.write(
        f"""
        My name is **{NAME}**, and I am currently
        pursuing **{PROGRAM}** at
        **{UNIVERSITY}**.

        I am a second-year college student under
        section **{SECTION}**.
        """
    )

    st.divider()

    st.subheader("📚 My Academic Journey")

    st.info(
        "From elementary education to college, "
        "I continue to pursue my academic goals "
        "and develop my knowledge and skills."
    )


# =====================================
# MY PROFILE PAGE
# =====================================

elif page == "My Profile":

    st.title("👤 My Personal Profile")

    st.write("Get to know more about me.")

    st.divider()

    col1, col2 = st.columns([1, 2])

    with col1:

        try:
            st.image("profile.jpg", width=220)
        except Exception:
            st.warning("Profile picture not found.")

    with col2:

        st.subheader(NAME)

        st.write("🎓 Mechanical Engineering Student")

        st.write("🏫 NEMSU - Bislig Campus")

        st.success("2nd Year | BSME 2B")

    st.divider()

    st.subheader("📋 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Full Name**")
        st.write(NAME)

        st.write("**Email Address**")
        st.write(EMAIL)

    with col2:
        st.write("**Birthday**")
        st.write(BIRTHDAY)

        st.write("**Year and Section**")
        st.write(f"{YEAR_LEVEL} - {SECTION}")

    st.divider()

    st.subheader("🎯 Current Academic Information")

    st.write(f"**Program:** {PROGRAM}")

    st.write(f"**University:** {UNIVERSITY}")


# =====================================
# EDUCATIONAL BACKGROUND PAGE
# =====================================

elif page == "Educational Background":

    st.title("🎓 Educational Background")

    st.write(
        "A timeline of my academic journey "
        "and educational achievements."
    )

    st.divider()

    education = [
        {
            "level": "Elementary Education",
            "school": "Mangagoy Hilltop Elementary School",
            "year": "2013 - 2019",
            "icon": "🏫"
        },
        {
            "level": "Junior High School",
            "school": "Tabon Maximino Estrella National High School",
            "year": "2019 - 2023",
            "icon": "📘"
        },
        {
            "level": "Senior High School",
            "school": "Tabon Maximino Estrella National High School",
            "year": "2023 - 2025",
            "icon": "📚"
        },
        {
            "level": "College Education",
            "school": "North Eastern Mindanao State University - Bislig Campus",
            "year": "2025 - Present",
            "icon": "🎓"
        }
    ]

    for item in education:

        with st.container(border=True):

            st.subheader(
                f"{item['icon']} {item['level']}"
            )

            st.write(f"**School:** {item['school']}")

            st.write(f"**School Years:** {item['year']}")

    st.divider()

    st.success(
        "Currently enrolled as a 2nd Year "
        "Bachelor of Science in Mechanical "
        "Engineering student (BSME 2B)."
    )


# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.markdown(
    '<div class="footer">'
    'Designed by Gerald Brandon Angus Seriño'
    '<br>Student Portfolio | 2026'
    '</div>',
    unsafe_allow_html=True
)
