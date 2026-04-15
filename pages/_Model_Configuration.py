import streamlit as st
import pandas as pd
from datetime import date, time

st.title("Model configuration & Inputs")
st.write("Configure the machine learning pipeline using interactive widgets.")

# file uploads
st.header("1. Data Ingestion")
# st.file_uploader allows users to upload files. Returns the file object or None.
uploaded_file = st.file_uploader("Upload Training Dataset (CSV)", type=['csv'])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    # We can immediately read the file because the script re-runs upon upload
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head(3))
else:
    st.info("Awaiting file upload...")

st.divider()

# Text, Numbers, and Selections
st.header("2. Algorithm Selection")

col1, col2 = st.columns(2)

with col1:
   # select  (Dropdown) - returns a string
   model_type = st.selectbox(
       "**Select Model Architecture**",
       options=['Random Forest', 'XGBoost', 'Neural Network', 'SVM'],
       index = 1 # Defaults to XGBoost
   )

   # multiselect - returns a list of strings
   features = st.multiselect(
       "Select Features to Include",
       options = ['age', 'income', 'education', 'credit_score', 'region'],
       default=['age', 'income', 'credit_score']
   )

with col2:
    # Number Input - returns a float or int
    threshold = st.number_input(
        "Classification Threshold",
        min_value =0.0, max_value = 1.0, value = 0.5, step = 0.01
    )

    # Radio buttons - returns a string
    split_method = st.radio(
        "Train/Test Split Method",
        options = ['Hold-out (80/20)', 'K-Fold CV'],
        horizontal = True
    )

    # Checkbox - returns a boolean (True/False)
    normalise = st.checkbox("Normalise features before training", value=True)
    

st.divider()

# Sliders
st.header("3. Hyperparameters & Filtering")

# Single slider - returns an integer/float
n_estimators = st.slider("Number of Tress", min_value = 10, max_value = 500, value = 100, step = 10)

# Range slider
# Range slider - returns a tuple (min_selected, max_selected)
age_filter = st.slider("Filter Training Data by Age", min_value=18, max_value=80, value=(25, 55))

st.write(f"**Current Configuration:** Training a `{model_type}` on users aged `{age_filter[0]}` to `{age_filter[1]}`.")

st.divider()

st.header("4. Execution")

# A button returns True ONLY on the exact script run where it was clicked.
# Otherwise, it is False.
if st.button("Initialize Training Pipeline", type="primary"):
    with st.spinner("Compiling model and starting training..."):
        # This is where your actual ML code would go!
        import time as pytime
        pytime.sleep(2) # Simulating work
    
    st.success(f"Successfully trained {model_type} with {n_estimators} trees!")
    
    # Create some dummy data to download
    results_csv = pd.DataFrame({'Prediction': [1, 0, 1], 'Confidence': [0.92, 0.81, 0.99]}).to_csv(index=False)
    
    # Download button triggers a file download
    st.download_button(
        label="📥 Download Predictions CSV",
        data=results_csv,
        file_name="model_predictions.csv",
        mime="text/csv"
    )