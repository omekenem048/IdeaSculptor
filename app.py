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
    tab1, tab2 = st.tabs(["🧩 Sculpt an Idea", "🗃️ Idea Vault"])

    # --- TAB 1: GUIDED IDEA BUILDER ---
    with tab1:
        st.markdown(f"<h3 style='color: {primary_color}; font-family: {selected_font};'>Step 1: The Messy Brain Dump</h3>", unsafe_allow_html=True)
        messy_input = st.text_area(
            "Type your raw, messy thoughts here (don't worry about grammar or sense!):",
            placeholder="e.g. want to make something for people who forget to drink water, maybe with game points or cute animals...",
            height=100
        )

        st.markdown(f"<h3 style='color: {primary_color}; font-family: {selected_font};'>Step 2: Unpick the Details</h3>", unsafe_allow_html=True)
        st.write("Answer these quick questions to give your thought shape:")

        col1, col2 = st.columns(2)
        with col1:
            target_audience = st.selectbox(
                "Who is this built for?",
                ["Students / Teenagers", "Gamers", "Busy Professionals", "Creatives / Artists", "Everyone!"]
            )
            project_type = st.selectbox(
                "What type of project is it?",
                ["Web App / Tool", "Game", "Mobile App", "Creative Writing / Content", "Physical Device"]
            )
        
        with col2:
            main_problem = st.text_input(
                "What problem does it fix?",
                placeholder="e.g. People forget habits easily."
            )
            special_feature = st.text_input(
                "What is the coolest / fun feature?",
                placeholder="e.g. Unlocking mini digital pets."
            )

        title_input = st.text_input("Give your idea a temporary cool title:", placeholder="e.g. HabitPets")

        st.divider()

        # Generate Pitch Card
        if st.button("✨ Sculpt My Pitch Card"):
            if title_input and main_problem and special_feature:
                # Build structured dictionary
                new_idea = {
                    "title": title_input,
                    "audience": target_audience,
                    "type": project_type,
                    "problem": main_problem,
                    "feature": special_feature,
                    "dump": messy_input if messy_input else "No raw dump provided."
                }
                
                # Save to temporary session state
                st.session_state.saved_ideas.append(new_idea)
                st.success("🎉 Idea sculpted and saved to your Vault!")
                st.balloons()
                
                # Display Formatted Card with dynamic primary color
                st.markdown(
                    f"""
                    <div style='background-color: #F8F9FA; border-left: 5px solid {primary_color}; padding: 20px; border-radius: 8px; margin-top: 15px; font-family: {selected_font};'>
                        <h2 style='color: {primary_color}; margin-top:0;'>🚀 {new_idea['title']}</h2>
                        <p><strong>🎯 Audience:</strong> {new_idea['audience']} | <strong>📦 Format:</strong> {new_idea['type']}</p>
                        <hr style='border: 0.5px solid #E0E0E0;'>
                        <p><strong>⚠️ The Problem:</strong> {new_idea['problem']}</p>
                        <p><strong>💡 Key Feature:</strong> {new_idea['feature']}</p>
                        <p style='color: #888888; font-size: 0.9rem;'><em>Raw Notes: "{new_idea['dump']}"</em></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.warning("Please fill in the title, problem, and key feature to sculpt your pitch card!")

    # --- TAB 2: IDEA VAULT ---
    with tab2:
        st.markdown(f"<h3 style='color: {primary_color}; font-family: {selected_font};'>🗃️ Your Saved Ideas Vault</h3>", unsafe_allow_html=True)
        
        if not st.session_state.saved_ideas:
            st.info("Your vault is empty! Head over to the 'Sculpt an Idea' tab to create your first pitch card.")
        else:
            st.write(f"You have **{len(st.session_state.saved_ideas)}** idea(s) stored in this session:")
            
            for idx, idea in enumerate(reversed(st.session_state.saved_ideas)):
                with st.expander(f"💡 {idea['title']} ({idea['type']})"):
                    st.write(f"**Target Audience:** {idea['audience']}")
                    st.write(f"**Problem Solved:** {idea['problem']}")
                    st.write(f"**Cool Feature:** {idea['feature']}")
                    st.caption(f"Raw Brain Dump: {idea['dump']}")
            
            if st.button("🗑️ Clear Vault"):
                st.session_state.saved_ideas = []
                st.rerun()




