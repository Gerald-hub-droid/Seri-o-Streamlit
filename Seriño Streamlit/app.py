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
