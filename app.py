import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="IdeaSculptor — Messy Thoughts to Clear Projects",
    page_icon="💡",
    layout="centered",
)

# --- SESSION STATE INITIALIZATION ---
if "entered" not in st.session_state:
    st.session_state.entered = False
if "username" not in st.session_state:
    st.session_state.username = "Innovator"
if "age" not in st.session_state:
    st.session_state.age = ""
if "role" not in st.session_state:
    st.session_state.role = ""
if "saved_ideas" not in st.session_state:
    st.session_state.saved_ideas = []

# Default Theme Customization Settings
if "theme_color" not in st.session_state:
    st.session_state.theme_color = "#6C5CE7" # Default Purple
if "font_style" not in st.session_state:
    st.session_state.font_style = "sans-serif"


# --- SCREEN 1: WELCOME / LANDING PAGE ---
if not st.session_state.entered:
    st.markdown(
        "<h1 style='text-align: center; color: #6C5CE7;'>💡 Welcome to IdeaSculptor</h1>", 
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size: 1.1rem; color: #555555;'>"
        "Turn your messy, half-baked thoughts into clean, structured project pitches!"
        "</p>", 
        unsafe_allow_html=True
    )
    st.divider()

    st.subheader("👋 Welcome! Let's get your workspace set up.")
    
    # User Profile Inputs
    name_input = st.text_input("Enter your Username / Name:", placeholder="e.g. Alex")
    
    col_a, col_b = st.columns(2)
    with col_a:
        age_input = st.number_input("Age (Optional):", min_value=5, max_value=120, value=18)
    with col_b:
        role_input = st.selectbox("What best describes you?", ["Student / Hacker", "Creator / Designer", "Developer", "Entrepreneur", "Other"])

    st.write("")
    if st.button("🚀 Enter Idea Studio", use_container_width=True):
        if name_input.strip():
            st.session_state.username = name_input
        st.session_state.age = age_input
        st.session_state.role = role_input
        st.session_state.entered = True
        st.rerun()

# --- SCREEN 2: MAIN IDEA STUDIO ---
else:
    # --- SIDEBAR THEME CUSTOMIZER ---
    with st.sidebar:
        st.header("🎨 Studio Settings")
        st.session_state.theme_color = st.color_picker(
            "Primary Accent Color:", 
            st.session_state.theme_color
        )
        st.session_state.font_style = st.selectbox(
            "Font Style:", 
            ["sans-serif", "serif", "monospace", "cursive"]
        )
        
        st.divider()
        st.write(f"👤 **Creator:** {st.session_state.username}")
        if st.session_state.role:
            st.write(f"🏷️ **Role:** {st.session_state.role}")
            
        if st.button("🔄 Change Profile"):
            st.session_state.entered = False
            st.rerun()

    # Dynamic CSS Variables based on sidebar settings
    primary_color = st.session_state.theme_color
    selected_font = st.session_state.font_style

    # --- MAIN APP HEADER ---
    st.markdown(
        f"<h1 style='text-align: center; color: {primary_color}; font-family: {selected_font}; font-weight: 700;'>"
        f"💡 IdeaSculptor"
        f"</h1>", 
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='text-align: center; color: #555555; font-size: 1.2rem; font-family: {selected_font}; margin-bottom: 25px;'>"
        f"Ready to unpick some thoughts, <strong>{st.session_state.username}</strong>? 🚀"
        f"</p>", 
        unsafe_allow_html=True
    )

    # Navigation Tabs
    tab1, tab2 = st.tabs(
