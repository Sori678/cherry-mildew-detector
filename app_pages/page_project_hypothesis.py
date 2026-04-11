import streamlit as st

def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")
    st.info(
        f"* We suspect cherry leaves with powdery mildew have clear marks, "
        f"typically white powdery patches, that can differentiate them from healthy leaves.")
    st.success(
        f"* We suspect cherry leaves with powdery mildew have clear marks, "
        f"typically white powdery patches, that can differentiate them from healthy leaves. \n\n"
        f"* An Image Montage shows that typically a powdery mildew leaf has white patches. "
        f"Average Image, Variability Image and Difference between Averages studies didn't "
        f"reveal a clear pattern to differentiate highlighting the need for a ML model.")