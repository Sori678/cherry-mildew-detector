import streamlit as st

def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.info(
        f"**Hypothesis**:\n"
        f"* We suspect that cherry leaves affected by powdery mildew present clear visual markers "
        f"that distinguish them from healthy leaves, such as light gray or white powdery patches.\n"
        f"* We believe a Convolutional Neural Network (CNN) is capable of detecting these spatial "
        f"patterns effectively for automated classification.")

    st.success(
        f"**Validation**:\n"
        f"* **Visual Study**: Our EDA (Exploratory Data Analysis) confirmed that infected leaves "
        f"show distinct white texture patterns. While the 'Average Image' study showed subtle "
        f"discolorations, the 'Variability Study' highlighted higher pixel variance in infected areas.\n"
        f"* **Model Performance**: The hypothesis was fully validated by the ML model, which achieved "
        f"an accuracy of over 99% on the test set. The model successfully learned to differentiate "
        f"between the two classes based on these specific fungal markers.")
    
    st.write("---")
    st.write("#### How to verify this?")
    st.info(
        f"1. Navigate to the **Cells Visualizer** page to see the average and variability images.\n"
        f"2. Use the **Image Montage** to see random samples of infected leaves and spot the white patches yourself.\n"
        f"3. Upload a leaf image in the **Mildew Detector** to see the model's hypothesis validation in real-time.")