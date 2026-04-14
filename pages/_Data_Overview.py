import streamlit as st

# we do not use st.set_page_config() here.
# that is only called once in app.py

st.title("System Data & Logs Overview")
st.write("This page demonstrates how to format text, code snippets, and systems metrics using streamlit's display elements.")

st.divider() # adds a horizontal line for clean separation

st.header("1. Documentation & Architecture")
st.markdown("""
**System Architecture Overview:**
            The current environment processes incoming data streams.
* *Primary Language:* Python 3.11
* *Documentation:* [Streamlit Docs](https://docs.streamlit.io)""")

st.subheader("Underlying Methematical Model")
st.latex(r'\hat{y} = \sigma(W \cdot x + b)')

st.divider()

# System Metrics
st.header("2. Live System Metrics")
st.markdown("Metrics are essential for monitoring performance at a glance.")

# Creating 3 columns for our metric cards
col1, col2, col3 = st.columns(3)

# delta_color="inverse" makes a negative number green (good for latency/loss)
col1.metric(label="Pipeline Success Rate", value="98.2%", delta="1.2%")
col2.metric(label="Server Latency", value="45ms", delta="-5ms", delta_color="inverse")
col3.metric(label="Active Users", value="1,204", delta="12")

st.divider()

# status notifications
st.header("3. Environment Status")

st.success("Database connection established successfully.")
st.info("System running in optimal state. 14,000 logs processed.")
st.warning("High memory usage detected on worker node 02.")
st.error("Critical: Build failed at Integration Testing stage.")

# A toast is a temporary pop-up in the bottom right
if st.button("Refresh System State"):
    st.toast("System state refreshed!", icon = "♾️")