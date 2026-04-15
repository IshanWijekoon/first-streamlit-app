import streamlit as st
import time

st.title("PulseCI: Pipeline Analyzer")
st.write("Identify root causes for CI/CD pipeline failures using log analysis.")

# 1. Sidebar 
# Everything inside this 'with' block goes to the left sidebar
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=50) # Placeholder logo
    st.header("PulseCI Controls")
    environment = st.selectbox("Pipeline Environment", ["Production", "Staging", "Development"])
    analyze_btn = st.button("Run Log Analysis", type="primary")
    st.divider()
    st.caption("PulseCI Engine v1.0")

# 2. Tabs
# We create two tabs to separate the high-level view from the deep dive
tab1, tab2 = st.tabs(["Dashboard Overview", "Root Cause Analysis"])

with tab1:
    st.subheader(f"Current Environment: {environment}")
    
    # 3. Columns
    # Using 'gap="large"' adds breathing room between the columns
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.metric("Total Builds", "1,204", "+15")
    with col2:
        st.metric("Failure Rate", "4.2%", "-0.5%", delta_color="inverse")
    with col3:
        st.metric("Avg Resolution Time", "14m", "-2m", delta_color="inverse")
        
    st.divider()
    
    # 4. Expanders
    # Keeps the UI clean by hiding raw logs until the user wants to see them
    with st.expander("View Raw Error Logs (Latest Build)", expanded=False):
        st.code("""
        [ERROR] 2026-04-15 14:32:05 - Build failed at step: Integration Tests
        [FATAL] memory limit exceeded on container 'test-runner'
        [INFO]  Shutting down pipeline...
        """, language="bash")

with tab2:
    st.subheader("Diagnostic Engine")
    st.write("Run the analysis from the sidebar to detect the root cause.")
    
    # 5. Status and Progress
    # We trigger this only if the button in the sidebar was clicked
    if analyze_btn:
        # st.status creates a neat, collapsible loading box for multi-step processes
        with st.status("Initializing PulseCI Diagnostics...", expanded=True) as status:
            st.write("Fetching artifacts from CI server...")
            time.sleep(1.5) # Simulating network request
            
            st.write("Parsing log structures...")
            time.sleep(1.5)
            
            st.write("Applying root-cause identification models...")
            time.sleep(1.5)
            
            # Update the status box when complete
            status.update(label="Analysis Complete!", state="complete", expanded=False)
            
        # Display the final result outside the status box
        st.error("**Root Cause Identified:** Container memory leak during the 'test-runner' execution phase.")
        st.info("**Recommended Action:** Increase the memory allocation for the test container from 2GB to 4GB in `docker-compose.yml`.")