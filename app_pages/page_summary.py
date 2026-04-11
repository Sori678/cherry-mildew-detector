import streamlit as st

def page_summary_body():
    st.write("### Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Cherry Powdery Mildew is a fungal disease caused by Podosphaera clandestina.\n"
        f"* It affects the leaves, providing a white powdery appearance.\n"
        f"* This project aims to automate the detection of this disease using Machine Learning.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset contains over 4,000 images of cherry leaves, "
        f"split between healthy and powdery mildew categories.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Sori678/cherry-mildew-detector).")

    st.success(
        f"**Business Requirements**\n"
        f"1. The client is interested in conducting a study to visually differentiate "
        f"a healthy cherry leaf from one with powdery mildew.\n"
        f"2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.")