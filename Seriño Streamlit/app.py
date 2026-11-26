import streamlit as st

st.set_page_config(
    page_title="Gerald | Personal Portfolio",
    layout="wide"
)

# ==========================================
# OWNER ACCOUNT
# ==========================================

OWNER_EMAIL = st.secrets["owner_email"].lower().strip()
OWNER_PASSWORD = st.secrets["owner_password"]

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

# ==========================================
# SESSION STATE
# ==========================================

defaults = {
    "screen": "intro",
    "authenticated": False,
    "current_user": None,
    "accounts": {},
    "profile_name": DEFAULT_NAME,
    "profile_email": DEFAULT_EMAIL,
    "profile_picture": None,
    "theme": "Light"
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

if OWNER_EMAIL not in st.session_state.accounts:
    st.session_state.accounts[OWNER_EMAIL] = {
        "password": OWNER_PASSWORD,
        "role": "Owner"
    }

# ==========================================
# THEMES
# ==========================================

themes = {
    "Light": {
        "background": "#FFFFFF",
        "surface": "#F4F4F4",
        "text": "#111111",
        "sidebar": "#EEEEEE",
        "border": "#DDDDDD"
    },
    "Dark": {
        "background": "#171717",
        "surface": "#242424",
        "text": "#FFFFFF",
        "sidebar": "#202020",
        "border": "#444444"
    },
    "Gray": {
        "background": "#DCDCDC",
        "surface": "#EEEEEE",
        "text": "#222222",
        "sidebar": "#C9C9C9",
        "border": "#BBBBBB"
    },
    "OLED Black": {
        "background": "#000000",
        "surface": "#111111",
        "text": "#FFFFFF",
        "sidebar": "#080808",
        "border": "#333333"
    }
}

theme = themes[st.session_state.theme]

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(f"""
<style>
.stApp {{
    background-color: {theme['background']};
    color: {theme['text']};
}}

section[data-testid="stSidebar"] {{
    background-color: {theme['sidebar']};
}}

h1, h2, h3 {{
    color: {theme['text']} !important;
}}

.stButton button {{
    border-radius: 8px;
    min-height: 42px;
    font-weight: 600;
}}

hr {{
    border-color: {theme['border']};
}}

.footer {{
    text-align: center;
    padding: 20px;
    font-size: 12px;
}}
</style>
""", unsafe_allow_html=True)

# ==========================================
# FUNCTIONS
# ==========================================

def logout():
    st.session_state.authenticated = False
    st.session_state.current_user = None
    st.session_state.screen = "intro"
    st.rerun()


def get_role():
    if not st.session_state.authenticated:
        return None

    account = st.session_state.accounts.get(
        st.session_state.current_user
    )

    return account["role"] if account else None


def is_owner():
    return get_role() == "Owner"


def is_admin():
    return get_role() in ["Owner", "Administrator"]


def show_clock():
    st.components.v1.html("""
    <div style="font-family:Arial;text-align:right;">
        <div id="clock" style="font-size:24px;font-weight:bold;"></div>
        <div id="date" style="font-size:13px;"></div>
        <div style="font-size:12px;">
            Asia/Manila (UTC+08:00)
        </div>
    </div>

    <script>
    function updateClock() {
        const now = new Date();

        document.getElementById("clock").textContent =
            new Intl.DateTimeFormat("en-US", {
                timeZone: "Asia/Manila",
                hour: "2-digit",
                minute: "2-digit",
                second: "2-digit",
                hour12: true
            }).format(now);

        document.getElementById("date").textContent =
            new Intl.DateTimeFormat("en-US", {
                timeZone: "Asia/Manila",
                weekday: "long",
                year: "numeric",
                month: "long",
                day: "numeric"
            }).format(now);
    }

    updateClock();
    setInterval(updateClock, 1000);
    </script>
    """, height=75)

# ==========================================
# INTRODUCTION SCREEN
# ==========================================

if st.session_state.screen == "intro":

    st.markdown("""
    <div style="
        background:#111111;
        color:white;
        padding:55px 35px;
        border-radius:18px;
        min-height:400px;
    ">
        <div style="
            font-size:14px;
            letter-spacing:4px;
            color:#AAAAAA;
        ">
            PERSONAL PORTFOLIO
        </div>

        <br><br>

        <div style="
            font-size:clamp(32px,6vw,58px);
            font-weight:700;
            line-height:1.2;
        ">
            Welcome to My<br>
            Digital Space.
        </div>

        <br>

        <div style="
            color:#BBBBBB;
            font-size:18px;
        ">
            Learning. Growing. Engineering.
        </div>

        <br>

        <div style="
            max-width:600px;
            color:#CCCCCC;
            line-height:1.8;
        ">
            Discover my academic journey, personal background,
            and experiences as a Mechanical Engineering student.
        </div>

        <br><br>

        <div style="
            font-size:14px;
            letter-spacing:2px;
        ">
            GERALD BRANDON ANGUS SERIÑO
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button(
            "ENTER PORTFOLIO",
            use_container_width=True
        ):

            st.session_state.screen = "login"
            st.rerun()

    st.markdown("""
    <div class="footer">
        PERSONAL STUDENT PORTFOLIO | 2026
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# LOGIN SCREEN
# ==========================================

elif st.session_state.screen == "login":

    st.title("Account Login")

    st.write("Sign in to access the portfolio.")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        with st.form("login_form"):

            email = st.text_input(
                "Email Address"
            ).lower().strip()

            password = st.text_input(
                "Password",
                type="password"
            )

            login = st.form_submit_button(
                "Sign In",
                use_container_width=True
            )

            if login:

                account = st.session_state.accounts.get(email)

                if account and account["password"] == password:

                    st.session_state.authenticated = True

                    st.session_state.current_user = email

                    st.session_state.screen = "main"

                    st.success("Login successful.")

                    st.rerun()

                else:

                    st.error("Invalid email or password.")

        st.divider()

        st.subheader("New Visitor?")

        if st.button(
            "Create Viewer Account",
            use_container_width=True
        ):

            st.session_state.screen = "register"

            st.rerun()

        if st.button(
            "Back to Introduction",
            use_container_width=True
        ):

            st.session_state.screen = "intro"

            st.rerun()


# ==========================================
# REGISTRATION SCREEN
# ==========================================

elif st.session_state.screen == "register":

    st.title("Create an Account")

    st.write(
        "Register to access the portfolio as a viewer."
    )

    with st.form("registration_form"):

        new_email = st.text_input(
            "Email Address"
        ).lower().strip()

        new_password = st.text_input(
            "Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        register = st.form_submit_button(
            "Register",
            use_container_width=True
        )

        if register:

            if not new_email or not new_password:

                st.error("Please complete all fields.")

            elif len(new_password) < 10:

                st.error(
                    "Password must contain at least 10 characters."
                )

            elif new_password != confirm_password:

                st.error("Passwords do not match.")

            elif new_email in st.session_state.accounts:

                st.error("This account already exists.")

            else:

                st.session_state.accounts[new_email] = {
                    "password": new_password,
                    "role": "Viewer"
                }

                st.success(
                    "Account created successfully. You can now log in."
                )

    if st.button("Back to Login"):

        st.session_state.screen = "login"

        st.rerun()
# ==========================================
# MAIN APPLICATION
# ==========================================

elif st.session_state.screen == "main":

    # Verify login
    if not st.session_state.authenticated:
        st.session_state.screen = "intro"
        st.rerun()

    current_role = get_role()

    if current_role is None:
        logout()

    # ======================================
    # VERTICAL SIDEBAR
    # ======================================

    with st.sidebar:

        st.markdown("## GERALD.")

        st.caption("PERSONAL PORTFOLIO")

        st.divider()

        st.markdown("### NAVIGATION")

        pages = [
            "Home",
            "About Developer"
        ]

        if is_admin():
            pages.append("Settings")

        if is_owner():
            pages.append("Administration")

        page = st.radio(
            "Select a page",
            pages,
            label_visibility="collapsed"
        )

        st.divider()

        st.markdown("### ACCOUNT")

        st.write(
            st.session_state.current_user
        )

        st.caption(
            "Role: " + current_role
        )

        st.divider()

        # PROFILE PICTURE

        if st.session_state.profile_picture:

            st.image(
                st.session_state.profile_picture,
                width=130
            )

        st.markdown(
            "**" + st.session_state.profile_name + "**"
        )

        st.caption(SECTION)

        st.divider()

        # LOGOUT

        if st.button(
            "Logout",
            use_container_width=True
        ):

            logout()

    # ======================================
    # MAIN HEADER
    # ======================================

    header_col, clock_col = st.columns([3, 1])

    with header_col:

        st.title("GERALD'S PORTFOLIO")

        st.caption(
            "A journey of learning, growth, and engineering."
        )

    with clock_col:

        show_clock()

    st.divider()

    # ======================================
    # HOME PAGE
    # ======================================

    if page == "Home":

        st.title("Home")

        st.write(
            f"Welcome, {st.session_state.profile_name}."
        )

        st.write(
            "Explore my personal information and academic journey."
        )

        st.divider()

        col1, col2 = st.columns([1, 2])

        with col1:

            if st.session_state.profile_picture:

                st.image(
                    st.session_state.profile_picture,
                    width=200
                )

            else:

                st.info(
                    "Profile picture not yet uploaded."
                )

        with col2:

            st.header(st.session_state.profile_name)

            st.write(
                "Mechanical Engineering Student"
            )

            st.write(UNIVERSITY)

            st.success(
                YEAR_LEVEL + " | " + SECTION
            )

        st.divider()

        st.header("Academic Overview")

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

        st.header("About This Portfolio")

        st.write("""
        This application presents my personal background,
        educational achievements, and journey as a
        Mechanical Engineering student.

        It serves as a digital representation of my
        academic development and personal growth.
        """)

    # ======================================
    # ABOUT DEVELOPER PAGE
    # ======================================

    elif page == "About Developer":

        st.title("About Developer")

        st.write(
            "Get to know the person behind this application."
        )

        st.divider()

        col1, col2 = st.columns([1, 2])

        with col1:

            if st.session_state.profile_picture:

                st.image(
                    st.session_state.profile_picture,
                    width=220
                )

        with col2:

            st.header(st.session_state.profile_name)

            st.write(PROGRAM)

            st.write(UNIVERSITY)

            st.write(
                "Year Level: " + YEAR_LEVEL
            )

            st.write(
                "Section: " + SECTION
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

            st.write("**Program**")

            st.write(PROGRAM)

        st.divider()

        st.header("Educational Background")

        education = [
            {
                "level": "Elementary Education",
                "school": "Mangagoy Hilltop Elementary School",
                "years": "2013 - 2019"
            },
            {
                "level": "Junior High School",
                "school": "Tabon Maximino Estrella National High School",
                "years": "2019 - 2023"
            },
            {
                "level": "Senior High School",
                "school": "Tabon Maximino Estrella National High School",
                "years": "2023 - 2025"
            },
            {
                "level": "College Education",
                "school": UNIVERSITY,
                "years": "2025 - Present"
            }
        ]

        for item in education:

            with st.container(border=True):

                st.subheader(item["level"])

                st.write(
                    "**School:** " + item["school"]
                )

                st.write(
                    "**Years:** " + item["years"]
                )

        st.divider()

        st.header("Academic Information")

        st.write("**University:** " + UNIVERSITY)

        st.write("**Program:** " + PROGRAM)

        st.write("**Year Level:** " + YEAR_LEVEL)

        st.write("**Section:** " + SECTION)

        st.divider()

        st.caption(
            "Developed by Gerald Brandon Angus Seriño."
        )

    # ======================================
    # FOOTER
    # ======================================

    st.divider()

    st.markdown("""
    <div class="footer">
        Developed by Gerald Brandon Angus Seriño
        <br>
        Personal Student Portfolio | 2026
    </div>
    """, unsafe_allow_html=True)
# ==========================================
# SETTINGS PAGE
# ==========================================

elif page == "Settings":

        if not is_admin():

            st.error("You are not authorized to access Settings.")

            st.stop()

        st.title("Settings")

        st.write(
            "Manage your portfolio appearance and information."
        )

        st.divider()

        # --------------------------------------
        # APPEARANCE SETTINGS
        # --------------------------------------

        st.header("Appearance")

        selected_theme = st.selectbox(
            "Choose Application Theme",
            ["Light", "Dark", "Gray", "OLED Black"],
            index=[
                "Light",
                "Dark",
                "Gray",
                "OLED Black"
            ].index(st.session_state.theme)
        )

        if st.button("Apply Theme"):

            st.session_state.theme = selected_theme

            st.success("Theme updated.")

            st.rerun()

        st.divider()

        # --------------------------------------
        # PROFILE SETTINGS
        # --------------------------------------

        st.header("Edit Developer Profile")

        with st.form("edit_profile"):

            edited_name = st.text_input(
                "Full Name",
                value=st.session_state.profile_name
            )

            edited_email = st.text_input(
                "Email Address",
                value=st.session_state.profile_email
            )

            save_profile = st.form_submit_button(
                "Save Profile"
            )

            if save_profile:

                if edited_name.strip() and edited_email.strip():

                    st.session_state.profile_name = (
                        edited_name.strip()
                    )

                    st.session_state.profile_email = (
                        edited_email.strip()
                    )

                    st.success("Profile updated.")

                    st.rerun()

                else:

                    st.error(
                        "Please complete all fields."
                    )

        st.divider()

        # --------------------------------------
        # PROFILE PICTURE
        # --------------------------------------

        st.header("Profile Picture")

        uploaded_picture = st.file_uploader(
            "Upload a new profile picture",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_picture:

            st.image(
                uploaded_picture,
                width=180
            )

            if st.button("Save Profile Picture"):

                st.session_state.profile_picture = (
                    uploaded_picture.getvalue()
                )

                st.success(
                    "Profile picture updated successfully."
                )

                st.rerun()

        st.divider()

        # --------------------------------------
        # APPLICATION INFORMATION
        # --------------------------------------

        st.header("Application Information")

        st.write(
            "**Application:** Gerald's Personal Portfolio"
        )

        st.write("**Version:** 1.0.0")

        st.write(
            "**Developer:** Gerald Brandon Angus Seriño"
        )

        st.write("**University:** " + UNIVERSITY)


# ==========================================
# ADMINISTRATION PAGE
# OWNER ONLY
# ==========================================

elif page == "Administration":

        if not is_owner():

            st.error(
                "Only the Owner can access Administration."
            )

            st.stop()

        st.title("Administration")

        st.write(
            "Manage registered accounts and administrator permissions."
        )

        st.divider()

        # --------------------------------------
        # ACCOUNT OVERVIEW
        # --------------------------------------

        st.header("Account Overview")

        total_accounts = len(
            st.session_state.accounts
        )

        total_admins = sum(
            1
            for account in st.session_state.accounts.values()
            if account["role"] == "Administrator"
        )

        total_viewers = sum(
            1
            for account in st.session_state.accounts.values()
            if account["role"] == "Viewer"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Total Accounts",
                total_accounts
            )

        with col2:

            st.metric(
                "Administrators",
                total_admins
            )

        with col3:

            st.metric(
                "Viewers",
                total_viewers
            )

        st.divider()

        # --------------------------------------
        # REGISTERED ACCOUNTS
        # --------------------------------------

        st.header("Registered Accounts")

        for email, account in st.session_state.accounts.items():

            with st.container(border=True):

                col1, col2 = st.columns([3, 1])

                with col1:

                    st.write("**" + email + "**")

                    st.caption(
                        "Role: " + account["role"]
                    )

                with col2:

                    if account["role"] == "Owner":

                        st.success("Owner")

                    elif account["role"] == "Administrator":

                        st.info("Administrator")

                    else:

                        st.write("Viewer")

        st.divider()

        # --------------------------------------
        # ASSIGN ADMINISTRATOR
        # --------------------------------------

        st.header("Administrator Management")

        available_accounts = [
            email
            for email, account in st.session_state.accounts.items()
            if account["role"] != "Owner"
        ]

        if available_accounts:

            selected_account = st.selectbox(
                "Select an account",
                available_accounts,
                key="admin_selected_account"
            )

            selected_role = st.session_state.accounts[
                selected_account
            ]["role"]

            st.write(
                "Current role: " + selected_role
            )

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "Promote to Administrator",
                    use_container_width=True
                ):

                    st.session_state.accounts[
                        selected_account
                    ]["role"] = "Administrator"

                    st.success(
                        "Administrator role assigned."
                    )

                    st.rerun()

            with col2:

                if st.button(
                    "Change to Viewer",
                    use_container_width=True
                ):

                    st.session_state.accounts[
                        selected_account
                    ]["role"] = "Viewer"

                    st.success(
                        "Viewer permissions restored."
                    )

                    st.rerun()

        else:

            st.info(
                "No additional accounts are registered yet."
            )

        st.divider()

        # --------------------------------------
        # PERMISSION INFORMATION
        # --------------------------------------

        st.header("Role Permissions")

        st.write("""
        **OWNER**
        - Complete application access.
        - Manage administrators.
        - Manage visitor accounts.
        - Edit developer profile.
        - Change application settings.

        **ADMINISTRATOR**
        - Access Settings.
        - Edit developer profile.
        - Upload profile pictures.
        - Change application themes.
        - Cannot appoint administrators.

        **VIEWER**
        - Access Home.
        - Access About Developer.
        - Cannot edit portfolio information.
        - Cannot access administrative settings.
        """)

        st.divider()

        st.caption(
            "Administrator privileges are controlled by the Owner."
        )

# ==========================================
# END OF APPLICATION
# ==========================================
