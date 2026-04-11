import streamlit as st
from app_pages.page_summary import page_summary_body
from app_pages.page_cells_visualizer import page_cells_visualizer_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_body

# Set page title and icon
st.set_page_config(page_title="Cherry Mildew Detector", page_icon="🍒")

# Dictionary to manage pages
pages = {
    "Project Summary": page_summary_body,
    "Cells Visualizer": page_cells_visualizer_body,
    "Mildew Detector": page_mildew_detector_body,
    "Project Hypothesis": page_project_hypothesis_body,
    "ML Performance": page_ml_performance_body,
}

# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Run the selected page function
pages[selection]()