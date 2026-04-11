import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread

def page_ml_performance_body():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")
    st.image(f"outputs/{version}/labels_distribution.png", caption='Labels Distribution')
    st.write("---")

    st.write("### Model Training History")
    col1, col2 = st.columns(2)
    with col1: 
        st.image(f"outputs/{version}/model_training_acc.png", caption='Model Training Accuracy')
    with col2:
        st.image(f"outputs/{version}/model_training_losses.png", caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(pd.read_pickle(f"outputs/{version}/test_evaluation.pkl"), index=['Loss', 'Accuracy']))