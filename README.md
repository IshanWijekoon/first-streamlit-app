# Intelligent System Dashboard
 This repository contains a professional, multi-page Proof-of-Concept (PoC) built with **Streamlit 1.56.0**. It is designed to demonstrate how machine learning models, data analysis pipelines, and interactive interfaces can be integrated into a single demonstrable web application.

## Project Structure
This project follows a modular and scalable architecture designed for production readiness:

- `app.py`: The main entry point and landing page.
- `pages/`: Automated multi-page routing for different project modules.
- `core/`: Backend Python logic, model utilities, and data processing.
- `data/`: Local storage for datasets (CSV/JSON).
- `models/`: Serialized machine learning models (.pkl/.h5).
- `.streamlit/`: Global configurations and secure secrets management.

## Features Implemented
- **Multi-page Navigation**: Organized flow between Data Overview and Model Configuration.
- **Interactive Widgets**: Real-time hyperparameter tuning using sliders, select boxes, and numerical inputs.
- **Dynamic Metrics**: Visual KPI cards for monitoring system performance and accuracy[cite: 151, 152].
- **Data Ingestion**: File upload capabilities for CSV training data.

## Installation & Setup To run this project locally, ensure you have **Python 3.11+** installed.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/IshanWijekoon/first-streamlit-app.git