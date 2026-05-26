# Cherry Mildew Detector

Cherry Mildew Detector is a Machine Learning web application developed to identify Powdery Mildew disease in cherry leaves using Deep Learning and Computer Vision techniques.

The application allows users to:
- analyze healthy and infected leaves,
- compare average and variability images,
- upload cherry leaf images,
- receive real-time predictions,
- review model performance metrics.

The project was developed using the CRISP-DM methodology and deployed with Streamlit and Heroku.

---

# Live Project

## Heroku Deployment

https://cherry-mildew-detector-sori-a62d7dccec61.herokuapp.com/

---

# GitHub Repository

https://github.com/Sori678/cherry-mildew-detector

---

# Business Understanding

## Project Background

Farmy & Foods is an agricultural company responsible for monitoring cherry plantations.

The company identified an increasing number of cherry leaves affected by Powdery Mildew, a fungal disease caused by *Podosphaera clandestina*.

Traditional manual inspection methods are:
- time-consuming,
- difficult to scale,
- dependent on human interpretation,
- prone to human error.

To improve disease detection efficiency and reduce crop losses, the company requested an intelligent image-classification system capable of automatically distinguishing healthy cherry leaves from infected leaves.

---

# Business Requirements

## Requirement 1 — Visual Study

The dashboard must:
- compare healthy and infected leaves,
- display average and variability images,
- provide image montage visualization.

## Requirement 2 — Disease Detection

The dashboard must:
- allow users to upload cherry leaf images,
- predict if the leaf is healthy or infected,
- provide accurate predictions.

---

# Dataset Content

The dataset contains RGB images of cherry leaves divided into two categories:
- Healthy
- Powdery Mildew

Dataset source:

https://www.kaggle.com/codeinstitute/cherry-leaves

---

# Dataset Distribution

| Category | Train | Validation | Test | Total |
|----------|------:|-----------:|-----:|------:|
| Healthy | 1472 | 211 | 421 | 2104 |
| Powdery Mildew | 1472 | 211 | 421 | 2104 |
| **Total** | **2944** | **422** | **842** | **4208** |

---

# Technologies Used

- Python
- Streamlit
- TensorFlow CPU
- Keras
- NumPy
- Pandas
- Plotly
- Matplotlib
- Seaborn
- Scikit-learn
- Pillow
- Joblib
- Heroku
- GitHub

---

# Dashboard Features

## Project Summary

This page presents:
- project background,
- business requirements,
- dataset information,
- dataset distribution.

![Project Summary](images/project%20summary.png)

---

## Cells Visualizer

This page allows users to:
- compare average images,
- analyze image variability,
- generate image montages.

### Average and Variability Study

![Cells Visualizer](images/cels%20visualizer.png)

### Healthy Leaf Average Image

![Healthy Leaf](images/cels%20visualizer1.png)

### Difference Between Healthy and Powdery Mildew Leaves

![Difference Image](images/cels%20visualiser%202.png)

### Powdery Mildew Montage

![Powdery Mildew Montage](images/cels%20visualizer%203.png)

### Healthy Leaf Montage

![Healthy Montage](images/cels%20visualizer%204.png)

---

## Mildew Detector

Users can:
- upload leaf images,
- receive real-time predictions,
- download prediction reports.

### Upload and Prediction System

![Mildew Detector](images/mildew%20detector.png)

### Prediction Result

![Prediction Result](images/mildew%20detector%201.png)

---

## Project Hypothesis and Validation

This page explains:
- project hypothesis,
- validation process,
- final conclusions.

![Project Hypothesis](images/Project%20Hypothesis%20and%20Validation.png)

---

## ML Performance Metrics

This page presents:
- dataset distribution,
- model accuracy,
- training history,
- model evaluation metrics.

### Dataset Distribution

![Model Performance](images/Model%20Performance%20Metrics.png)

### Training Accuracy and Loss

![Training Metrics](images/Model%20Performance%20Metrics%201.png)

### Final Model Accuracy

![Final Accuracy](images/Model%20Performance%20Metrics%202.png)

---

# Machine Learning Model

A Convolutional Neural Network (CNN) was used for binary image classification.

The model was trained to distinguish:
- healthy cherry leaves,
- powdery mildew infected leaves.

Final test accuracy:
- 99.44%

The project successfully exceeded the business requirement of 97% accuracy.

---

# Project Hypothesis and Validation

## Hypothesis

Cherry leaves affected by Powdery Mildew present visible visual markers such as:
- white fungal patches,
- discoloration,
- texture inconsistencies.

We also hypothesize that a Convolutional Neural Network can learn these visual patterns and classify infected leaves with high accuracy.

---

## Validation

The hypothesis was validated through:
- Exploratory Data Analysis,
- average image analysis,
- variability analysis,
- image montage inspection,
- CNN model evaluation.

The final CNN model achieved over 99% accuracy on the test dataset, confirming that the disease patterns are visually distinguishable and suitable for automated classification.

---

# Business Conclusions

The project successfully achieved both business requirements defined by Farmy & Foods.

## Requirement 1 — Visual Study

The visual analysis tools demonstrated clear visual differences between healthy leaves and leaves affected by Powdery Mildew:
- average image analysis revealed visible discoloration patterns,
- variability analysis highlighted texture inconsistencies,
- image montage inspection confirmed visible fungal patterns.

These findings validate that Powdery Mildew produces identifiable visual markers that can support disease monitoring.

---

## Requirement 2 — Automated Disease Detection

The CNN classification model achieved 99.44% accuracy on unseen test data, exceeding the original target of 97%.

The deployed dashboard allows users to:
- upload cherry leaf images,
- receive instant predictions,
- review prediction confidence,
- support rapid disease identification.

The final system can help reduce manual inspection time and improve disease monitoring efficiency in agricultural environments.

---

# Actionable Insights

The project provides the following actionable insights:

1. Powdery Mildew can be visually distinguished from healthy leaves using image analysis.
2. The balanced dataset supports reliable model training and reduces class bias.
3. The CNN model exceeds the required business accuracy threshold.
4. The dashboard provides a practical tool for early disease detection.
5. The visual and predictive outputs support faster decision-making for plantation monitoring.

---

# Testing

## Manual Testing

| Feature | Result |
|---|---|
| Navigation Menu | PASS |
| Cells Visualizer | PASS |
| Image Montage | PASS |
| Image Upload Prediction | PASS |
| Model Performance Charts | PASS |

---

## Responsive Testing

The application was tested successfully on:
- Mobile devices
- Tablets
- Desktop screens

All pages display correctly across different screen sizes.

---

# Fixed Bugs

| Bug | Fix |
|---|---|
| FileNotFoundError during deployment | Fixed project paths and dataset structure |
| Heroku slug too large | Replaced TensorFlow with tensorflow-cpu |
| Missing montage images | Fixed dataset deployment paths |
| Plot rendering issues | Added proper output image paths |
| Dashboard deployment failures | Corrected Heroku deployment configuration |
## Remaining Bugs

No known bugs remaining.

---

# Deployment

## Heroku Deployment Steps

1. Create a Heroku application.
2. Connect the GitHub repository.
3. Add the required dependencies.
4. Create:
   - requirements.txt
   - Procfile
   - setup.sh
5. Deploy from the main branch.
6. Open the deployed application.

---

# Local Deployment

## Clone Repository

git clone https://github.com/Sori678/cherry-mildew-detector.git

## Install Dependencies

pip install -r requirements.txt

## Run Application

streamlit run app.py


---

# CRISP-DM Methodology

The project follows the CRISP-DM process:
1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

---

# Future Features

Possible future improvements:
- Multi-disease detection
- Mobile application
- Camera image detection
- Farmer analytics dashboard
- Cloud storage integration
- Batch image prediction

---

# Credits

## Dataset

- Code Institute
- Kaggle Cherry Leaves Dataset

## Libraries and Documentation

- Streamlit Documentation
- TensorFlow Documentation
- Plotly Documentation

---

# Author

Developed by Sorin Bivol