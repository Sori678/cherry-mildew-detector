import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
import os

def page_ml_performance_body():
    version = 'v1'

    st.write("### Model Performance Metrics")
    st.info(
        f"**Goal**: The model was trained to achieve a minimum accuracy of 97% on the test set. "
        f"Below we analyze the distribution of data and the learning progress of the CNN.")

    # --- Section 1: Labels Distribution ---
    st.write("### Train, Validation and Test Set: Labels Frequencies")
    labels_dist_path = f"outputs/{version}/labels_distribution.png"
    if os.path.exists(labels_dist_path):
        st.image(labels_dist_path, caption='Labels Distribution')
    else:
        st.warning("Labels distribution plot not found in the outputs folder.")
    
    st.write(
        f"The dataset is perfectly balanced, with an equal number of healthy and mildew-infected "
        f"images across all sets. This ensures the model does not develop a bias.")
    st.write("---")

    # --- Section 2: Training History ---
    st.write("### Model Training History")
    col1, col2 = st.columns(2)
    acc_path = f"outputs/{version}/model_training_acc.png"
    loss_path = f"outputs/{version}/model_training_losses.png"

    with col1: 
        if os.path.exists(acc_path):
            st.image(acc_path, caption='Model Training Accuracy')
        else:
            st.warning("Accuracy plot not found.")
    with col2:
        if os.path.exists(loss_path):
            st.image(loss_path, caption='Model Training Losses')
        else:
            st.warning("Loss plot not found.")
    
    st.success(
        f"**Analysis**:\n"
        f"* **Accuracy**: Both training and validation accuracy reach nearly 100%, showing excellent learning capacity.\n"
        f"* **Loss**: The loss curves decrease steadily, indicating a stable training process.\n"
        f"* **Overfitting**: No evidence of significant overfitting as validation follows training closely.")
    st.write("---")

    # --- Section 3: Test Set Performance ---
    st.write("### Generalised Performance on Test Set")
    st.table({
        "Metric": ["Loss", "Accuracy"],
        "Value": ["0.0210", "0.9944"]
    })

    st.info(
        f"The final accuracy on the unseen test set is **99.44%**. "
        f"This exceeds the target requirement of 97%, making the model reliable for industrial use.")