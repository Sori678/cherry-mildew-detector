import streamlit as st
import os
import pandas as pd
import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
import random

def page_cells_visualizer_body():
    st.write("### Cells Visualizer")
    st.info(
        f"**Business Requirement 1**: The client is interested in conducting a study to visually "
        f"differentiate a healthy cherry leaf from one with powdery mildew.")
    
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
            f"* This study highlights the subtle discolorations and texture changes "
            f"between the two categories.")
        st.image(diff_between_avgs, caption='Difference between average images')

    # Image Montage Logic
    if st.checkbox("Image Montage"): 
        st.write("* To view the montage, select a label and click the 'Create Montage' button")
        
        data_dir = 'inputs/cherry-leaves/test' # Verifică dacă aceasta este calea ta corectă
        labels = os.listdir(data_dir)
        label_to_display = st.selectbox("Select label", labels)
        
        if st.button("Create Montage"):
            create_montage(dir_path=data_dir, 
                           label_to_display=label_to_display, 
                           nrows=3, ncols=3, figsize=(10, 10))

def create_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
    """Generates an image montage of random leaf samples."""
    images_list = os.listdir(os.path.join(dir_path, label_to_display))
    if len(images_list) < nrows * ncols:
        st.error("Not enough images in the folder to create a montage.")
        return

    img_idx = random.sample(images_list, nrows * ncols)
    
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    for x in range(0, nrows * ncols):
        img = imread(os.path.join(dir_path, label_to_display, img_idx[x]))
        img_shape = img.shape
        axes.flatten()[x].imshow(img)
        axes.flatten()[x].set_title(f"W: {img_shape[1]}px | H: {img_shape[0]}px")
        axes.flatten()[x].axis('off')
    
    plt.tight_layout()
    st.pyplot(fig)