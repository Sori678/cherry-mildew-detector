import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import joblib
import os
import base64

def download_dataframe_as_csv(df):
    """Generates a link to download the analysis report as a CSV file."""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    # Create the HTML tag for the download link
    href = f'<a href="data:file/csv;base64,{b64}" download="mildew_detection_report.csv">Download Analysis Report</a>'
    return href

def page_mildew_detector_body():
    st.write("### Mildew Detector")
    
    st.info(
        f"**Business Requirement 2**: The client is interested in predicting if a cherry leaf is healthy "
        f"or contains powdery mildew based on an uploaded image.")

    st.write(
        f"You can download a set of healthy and mildew leaves for live testing from "
        f"[here](https://www.kaggle.com/codeinstitute/cherry-leaves).")

    images_buffer = st.file_uploader('Upload leaf images (PNG, JPG, JPEG)', 
                                    type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if images_buffer:
        version = 'v1'
        # We use os.path.join for maximum compatibility between systems
        model_path = os.path.join(os.getcwd(), 'outputs', version, 'cherry_leaves_model.h5')
        image_shape_path = os.path.join(os.getcwd(), 'outputs', version, 'image_shape.pkl')
        class_indices_path = os.path.join(os.getcwd(), 'outputs', version, 'class_indices.pkl')

        # Load resources
        model = load_model(model_path)
        image_shape = joblib.load(image_shape_path)
        class_indices = joblib.load(class_indices_path)
        labels_map = {v: k for k, v in class_indices.items()}

        all_results = [] 

        for img_file in images_buffer:
            img_pil = Image.open(img_file)
            st.image(img_pil, caption=f"Image: {img_file.name}")
            
            # Preprocessing
            img_resized = img_pil.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
            img_array = image.img_to_array(img_resized) / 255
            img_array = np.expand_dims(img_array, axis=0)

            # Prediction
            pred_proba = model.predict(img_array)[0][0]
            pred_class = (pred_proba > 0.5).astype("int32")
            pred_label = labels_map[pred_class].replace('_', ' ')

            # Display Result
            if pred_label == 'healthy':
                st.success(f"**Prediction: {pred_label.capitalize()}** (Probability: {pred_proba:.4f})")
            else:
                st.error(f"**Prediction: {pred_label.capitalize()}** (Probability: {pred_proba:.4f})")
            
            all_results.append({"Name": img_file.name, "Result": pred_label, "Probability": f"{pred_proba:.4f}"})
        
        # Summary Report
        if all_results:
            st.write("---")
            st.write("#### Analysis Report Summary")
            table_report = pd.DataFrame(all_results)
            st.table(table_report)
            
            st.markdown(download_dataframe_as_csv(table_report), unsafe_allow_html=True)