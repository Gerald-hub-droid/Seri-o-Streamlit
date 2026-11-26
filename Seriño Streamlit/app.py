
import streamlit as st
from pathlib import Path

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Gerald | Student Portfolio",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# PERSONAL INFORMATION
# ==========================================

DEFAULT_NAME = "Gerald Brandon Angus Seriño"
DEFAULT_EMAIL = "serinogeraldbrandon@gmail.com"

BIRTHDAY = "August 09, 2007"

PROGRAM = "Bachelor of Science in Mechanical Engineering"

UNIVERSITY = (
    "North Eastern Mindanao State University - Bislig Campus"
)

YEAR_LEVEL = "2nd Year"
SECTION = "BSME 2B"

PROFILE_IMAGE = Path("profile.jpg")

# ==========================================
# SESSION STATE
# ==========================================

if "profile_name" not in st.session_state:
    st.session_state.profile_name = DEFAULT_NAME

if "profile_email" not in st.session_state:
    st.session_state.profile_email = DEFAULT_EMAIL

if "appearance" not in st.session_state:
    st.session_state.appearance = "Light"

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* Main application */
.stApp {
    background-color: #F4F6FA;
}

/* Main content */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
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
    font-weight: 650;
}

/* Sidebar profile image */
section[data-testid="stSidebar"] img {
    border-radius: 12px;
}

/* Main profile image */
div[data-testid="stImage"] img {
    border-radius: 12px;
}

/* Information cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: white;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
}

/* Buttons */
.stButton button,
.stFormSubmitButton button {
    border-radius: 8px;
    font-weight: 600;
}

/* Radio buttons */
section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 10px;
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

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("## MY PORTFOLIO")
    st.caption("STUDENT PERSONAL WEBSITE")

    st.divider()

    # Profile picture
    if PROFILE_IMAGE.exists():

        st.image(
            str(PROFILE_IMAGE),
            width=180
        )

    else:

        st.warning(
            "Please upload your profile picture in Settings."
        )

    # Profile name
    st.markdown(
        f"### {st.session_state.profile_name}"
    )

    st.caption("Mechanical Engineering Student")

    st.caption(SECTION)

    st.divider()

    # Contact information
    st.markdown("### CONTACT")

    st.caption("EMAIL ADDRESS")

    st.write(st.session_state.profile_email)

    st.divider()

    # Navigation
    st.markdown("### NAVIGATION")

    page = st.radio(
        "Choose a page:",
        [
            "Home",
            "My Profile",
            "Educational Background",
            "Settings"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.caption("NEMSU - BISLIG CAMPUS")

    st.caption(
        "© 2026 Gerald Brandon Angus Seriño"
    )

# ==========================================
# HOME PAGE
# ==========================================

if page == "Home":

    st.title("Welcome to My Portfolio")

    st.subheader(
        f"Hello! I'm {st.session_state.profile_name}."
    )

    st.write(
        """
        Welcome to my personal student portfolio.

        This website provides information about me,
        my educational background, and my current
        academic journey as a Mechanical Engineering
        student.
        """
    )

    st.divider()

    # Overview cards
    col1, col2, col3 = st.columns(3)

    with col1:

        with st.container(border=True):

            st.caption("YEAR LEVEL")

            st.subheader("2nd Year")

            st.caption("Current academic level")

    with col2:

        with st.container(border=True):

            st.caption("PROGRAM")

            st.subheader("BSME")

            st.caption("Mechanical Engineering")

    with col3:

        with st.container(border=True):

            st.caption("SECTION")

            st.subheader("BSME 2B")

            st.caption("Current section")

    st.divider()

    st.header("About Me")

    st.write(
        f"""
        My name is **{st.session_state.profile_name}**.

        I am currently pursuing **{PROGRAM}** at
        **{UNIVERSITY}**.

        I am a second-year college student under
        section **{SECTION}**.

        This portfolio serves as an introduction to
        my personal information and educational
        achievements.
        """
    )

    st.divider()

    st.header("Current Academic Information")

    with st.container(border=True):

        st.write(f"**University:** {UNIVERSITY}")

        st.write(f"**Program:** {PROGRAM}")

        st.write(f"**Year Level:** {YEAR_LEVEL}")

        st.write(f"**Section:** {SECTION}")


# ==========================================
# MY PROFILE PAGE
# ==========================================

elif page == "My Profile":

    st.title("My Personal Profile")

    st.write(
        "Get to know more about my personal and academic information."
    )

    st.divider()

    col1, col2 = st.columns([1, 2])

    with col1:

        if PROFILE_IMAGE.exists():

            st.image(
                str(PROFILE_IMAGE),
                width=220
            )

        else:

            st.info(
                "No profile picture uploaded yet."
            )

    with col2:

        st.header(st.session_state.profile_name)

        st.write(
            "Bachelor of Science in Mechanical Engineering"
        )

        st.write(UNIVERSITY)

        st.success(
            "Currently Enrolled | BSME 2B"
        )

    st.divider()

    st.header("Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Full Name**")

        st.write(st.session_state.profile_name)

        st.write("**Email Address**")

        st.write(st.session_state.profile_email)

    with col2:

        st.write("**Birthday**")

        st.write(BIRTHDAY)

        st.write("**Year and Section**")

        st.write(f"{YEAR_LEVEL} - {SECTION}")

    st.divider()

    st.header("Academic Information")

    with st.container(border=True):

        st.write(f"**Program:** {PROGRAM}")

        st.write(f"**University:** {UNIVERSITY}")

        st.write(f"**Year Level:** {YEAR_LEVEL}")

        st.write(f"**Section:** {SECTION}")


# ==========================================
# EDUCATIONAL BACKGROUND PAGE
# ==========================================

elif page == "Educational Background":

    st.title("Educational Background")

    st.write(
        """
        This section presents my academic journey
        from elementary education to my current
        college studies.
        """
    )

    st.divider()

    education = [

        {
            "level": "Elementary Education",
            "school": "Mangagoy Hilltop Elementary School",
            "year": "2013 - 2019"
        },

        {
            "level": "Junior High School",
            "school": "Tabon Maximino Estrella National High School",
            "year": "2019 - 2023"
        },

        {
            "level": "Senior High School",
            "school": "Tabon Maximino Estrella National High School",
            "year": "2023 - 2025"
        },

        {
            "level": "College Education",
            "school": "North Eastern Mindanao State University - Bislig Campus",
            "year": "2025 - Present"
        }

    ]

    for item in education:

        with st.container(border=True):

            st.subheader(item["level"])

            st.write(
                f"**School:** {item['school']}"
            )

            st.write(
                f"**School Years:** {item['year']}"
            )

    st.divider()

    st.header("Current Academic Status")

    st.success(
        "Currently enrolled as a second-year "
        "Bachelor of Science in Mechanical "
        "Engineering student (BSME 2B)."
    )


# ==========================================
# SETTINGS PAGE
# ==========================================

elif page == "Settings":

    st.title("Settings")

    st.write(
        """
        Manage your personal information,
        profile picture, and application preferences.
        """
    )

    st.divider()

    # PROFILE SETTINGS
    st.header("Profile Settings")

    with st.form("profile_settings"):

        new_name = st.text_input(
            "Full Name",
            value=st.session_state.profile_name
        )

        new_email = st.text_input(
            "Email Address",
            value=st.session_state.profile_email
        )

        save_profile = st.form_submit_button(
            "Save Profile Changes",
            use_container_width=True
        )

        if save_profile:

            if not new_name.strip() or not new_email.strip():

                st.error(
                    "Please fill in both fields."
                )

            else:

                st.session_state.profile_name = new_name.strip()

                st.session_state.profile_email = new_email.strip()

                st.success(
                    "Your profile information has been updated."
                )

    st.divider()

    # PROFILE PICTURE SETTINGS
    st.header("Profile Picture")

    if PROFILE_IMAGE.exists():

        st.image(
            str(PROFILE_IMAGE),
            width=160,
            caption="Current Profile Picture"
        )

    uploaded_picture = st.file_uploader(
        "Upload a new profile picture",
        type=["jpg", "jpeg", "png"],
        help="Choose a JPG or PNG image."
    )

    if uploaded_picture is not None:

        st.image(
            uploaded_picture,
            width=160,
            caption="New Profile Picture Preview"
        )

        if st.button(
            "Update Profile Picture",
            use_container_width=True
        ):

            PROFILE_IMAGE.write_bytes(
                uploaded_picture.getvalue()
            )

            st.success(
                "Your profile picture has been updated."
            )

            st.rerun()

    st.divider()

    # APPEARANCE SETTINGS
    st.header("Appearance")

    selected_theme = st.selectbox(
        "Preferred Appearance",
        ["Light", "Dark"],
        index=(
            0 if st.session_state.appearance == "Light"
            else 1
        )
    )

    if st.button(
        "Save Appearance Preference"
    ):

        st.session_state.appearance = selected_theme

        st.success(
            f"{selected_theme} appearance preference saved."
        )

    st.caption(
        "This preference is saved for the current session. "
        "To change the complete Streamlit interface theme, "
        "configure the Streamlit theme separately."
    )

    st.divider()

    # ABOUT APPLICATION
    st.header("About This Application")

    with st.container(border=True):

        st.write(
            "**Application Name:** Gerald's Student Portfolio"
        )

        st.write(
            "**Version:** 1.0.0"
        )

        st.write(
            "**Developer:** Gerald Brandon Angus Seriño"
        )

        st.write(
            f"**University:** {UNIVERSITY}"
        )

        st.write(
            f"**Program:** {PROGRAM}"
        )

    st.divider()

    st.caption(
        "Your portfolio settings and profile information."
    )


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        Designed and Developed by Gerald Brandon Angus Seriño
        <br>
        Student Personal Portfolio | 2026
    </div>
    """,
    unsafe_allow_html=True
)
