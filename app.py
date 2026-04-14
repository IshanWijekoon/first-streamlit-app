import streamlit as st

# Page configuration
st.set_page_config(
            page_title = "My Intelligent System",
            page_icon = "🔑",
            layout = "wide",
            initial_sidebar_state = "expanded")

# Main title
st.title("Welcome to the Intelligent System Dashboard")
st.write("Environment setup is complete. This is the main entry point.")

col1, col2 = st.columns(2)
with col1:
    st.info("Project Structure Initialized")
with col2:
    st.success("Dependencies Installed")