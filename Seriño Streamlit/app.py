import streamlit as st

st.set_page_config(
    page_title="My App",
    layout="wide"
)

# Sidebar profile
with st.sidebar:
    st.image(
        "profile.jpg",
        width=120
    )

    st.markdown("Gerald Brandon Angus Seriño")
    st.caption("Administrator")
    st.divider()

    st.markdown("**Profile Information**")
    st.write("📧 serinogeraldbrandon@gmail.com")

    st.divider()

    st.markdown("### Navigation")
    page = st.radio(
        "Go to",
        ["Home", "Dashboard", "Profile", "Settings"]
    )
