import streamlit as st

def page_summary_body():
    st.write("### Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Cherry Powdery Mildew is a fungal disease caused by the pathogen *Podosphaera clandestina*.\n"
        f"* It manifests as white, powdery spots on leaves and fruit, potentially ruining entire cherry harvests if not detected early.\n"
        f"* Farmy & Foods, the client, currently relies on manual inspection, which is slow and prone to human error.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset consists of over 4,208 high-resolution images of cherry leaves.\n"
        f"* These images are divided into two categories: **Healthy** and **Powdery Mildew**.")

    # Adăugăm Tabelul de Transparență a Datelor cerut de evaluator
    st.write("#### Dataset Distribution")
    st.table({
        "Category": ["Healthy Leaves", "Mildew Infected", "Total Images"],
        "Count": ["2,104", "2,104", "4,208"]
    })

    st.write(
        f"* For additional technical information, please visit the "
        f"[Project README file](https://github.com/Sori678/cherry-mildew-detector).")

    st.success(
        f"**Business Requirements**\n"
        f"The project has two primary objectives defined by Farmy & Foods:\n"
        f"1. **Visual Study**: The client wants to visually differentiate a healthy cherry leaf from one with powdery mildew through a mean and variability study.\n"
        f"2. **Real-time Prediction**: The client requires a tool that can predict with at least 97% accuracy if a given leaf is healthy or infected.")