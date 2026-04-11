import streamlit as st
import os
import pandas as pd
import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt

def page_cells_visualizer_body():
    st.write("### Cells Visualizer")
    st.info(
        f"* The client is interested in conducting a study to visually differentiate "
        f"a healthy cherry leaf from one with powdery mildew.")
    
    version = 'v1'
    
    # Checkbox for Average and Variability images
    if st.checkbox("Difference between average and variability image"):
        avg_powdery_mildew = imread(f"outputs/{version}/avg_diff_powdery_mildew.png")
        avg_healthy = imread(f"outputs/{version}/avg_diff_healthy.png")

        st.warning(
            f"* We noticed typical patterns for powdery mildew as white cloudy patches, "
            f"while healthy leaves are clear green.")

        st.image(avg_powdery_mildew, caption='Powdery Mildew - Average and Variability')
        st.image(avg_healthy, caption='Healthy Leaf - Average and Variability')
        st.write("---")

    # Checkbox for Difference between averages
    if st.checkbox("Differences between average healthy and average powdery mildew leaves"):
        diff_between_avgs = imread(f"outputs/{version}/avg_diff.png")

        st.warning(
            f"* This study shows the visual difference between the two categories.")
        st.image(diff_between_avgs, caption='Difference between average images')

    # Placeholder for Montage
    if st.checkbox("Image Montage"): 
        st.write("* To view the montage, click on the 'Create Montage' button")
        st.info("Feature to be implemented.")