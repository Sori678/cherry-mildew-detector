import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import joblib

def page_mildew_detector_body():
    st.write("### Mildew Detector")
    st.info("Upload leaf images to predict if they are healthy or have powdery mildew.")

    images_buffer = st.file_uploader('Upload leaf images', type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if images_buffer:
        version = 'v1'
        model = load_model(f"outputs/{version}/cherry_leaves_model.h5")
        image_shape = joblib.load(f"outputs/{version}/image_shape.pkl")
        class_indices = joblib.load(f"outputs/{version}/class_indices.pkl")
        labels_map = {v: k for k, v in class_indices.items()}

        # IMPORTANT: Here we are using a simple LIST, not a DataFrame
        all_results = [] 

        for img_file in images_buffer:
            img_pil = Image.open(img_file)
            st.image(img_pil, caption=f"Image: {img_file.name}")
            
            img_resized = img_pil.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
            img_array = image.img_to_array(img_resized) / 255
            img_array = np.expand_dims(img_array, axis=0)

            pred_proba = model.predict(img_array)[0][0]
            pred_class = (pred_proba > 0.5).astype("int32")
            pred_label = labels_map[pred_class].replace('_', ' ')

            st.write(f"**Prediction: {pred_label.capitalize()}**")
            st.write(f"Probability: {pred_proba:.4f}")
            
            # Add the data to the standard Python list
            all_results.append({"Name": img_file.name, "Result": pred_label})

        # Only at the end do we convert the list into a table
        if all_results:
            st.success("Analysis Report")
            table_report = pd.DataFrame(all_results)
            st.table(table_report)