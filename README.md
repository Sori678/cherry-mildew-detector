# Mildew Detection in Cherry Leaves

This Machine Learning project was developed to detect Powdery Mildew disease in cherry leaves using Computer Vision and Deep Learning techniques.

The application allows users to:
- visually analyze healthy and infected leaves,
- explore image variability and average image comparisons,
- upload leaf images for real-time prediction,
- evaluate model performance through interactive visualizations.

The project was developed using the CRISP-DM methodology and deployed as a Streamlit dashboard.

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

## Requirement 1 — Visual Differentiation Study

The client requires a visual study capable of:
- differentiating healthy cherry leaves from infected leaves,
- identifying common visual patterns associated with Powdery Mildew,
- supporting disease analysis through image visualization techniques.

The visual study includes:
- average image analysis,
- variability analysis,
- image montage visualization.

---

## Requirement 2 — Automated Mildew Detection

The client requires a Machine Learning system capable of:
- receiving uploaded cherry leaf images,
- predicting whether the leaf is healthy or infected,
- achieving at least 97% prediction accuracy.

The final solution must be accessible through an interactive Streamlit dashboard.

---

# Dataset Content

## Dataset Source

The dataset was sourced from the Code Institute Kaggle repository:

https://www.kaggle.com/codeinstitute/cherry-leaves

---

## Dataset Description

The dataset contains RGB images of cherry leaves divided into two categories:
- Healthy Leaves
- Powdery Mildew Infected Leaves

The dataset was preprocessed and organized into:
- training set,
- validation set,
- test set.

---

# Dataset Distribution

| Category | Train | Validation | Test | Total |
|----------|------:|-----------:|-----:|------:|
| Healthy | 1472 | 211 | 421 | 2104 |
| Powdery Mildew | 1472 | 211 | 421 | 2104 |
| **Total** | **2944** | **422** | **842** | **4208** |

---

# Dataset Characteristics

- Image Type: RGB Images
- Total Images: 4,208
- Classification Type: Binary Classification
- Dataset Balance: Balanced
- Image Subject: Cherry Leaves
- Disease Target: Powdery Mildew

The dataset is balanced, which helps reduce prediction bias during model training.

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

# CRISP-DM Methodology

The project follows the CRISP-DM methodology:

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

---

# User Stories

| User Story ID | User Story | Business Requirement |
|---|---|---|
| US1 | As a user, I want to understand the project background and dataset information. | BR1 |
| US2 | As a user, I want to visually compare healthy and infected leaves. | BR1 |
| US3 | As a user, I want to inspect image montages and variability studies. | BR1 |
| US4 | As a user, I want to upload leaf images and receive predictions. | BR2 |
| US5 | As a user, I want to review model performance metrics and training history. | BR2 |

---

# Machine Learning Business Logic

## Visual Analysis

The project performs visual analysis through:
- average image comparison,
- variability analysis,
- image montage generation.

These techniques help identify visual differences between healthy and infected leaves.

---

## CNN Classification Model

A Convolutional Neural Network was developed for binary image classification.

The model:
- receives cherry leaf images,
- processes image patterns,
- predicts whether the leaf is healthy or infected.

The model achieved excellent accuracy while maintaining stable validation performance.

---

# Dashboard Features

The Streamlit dashboard includes:

## Project Summary
- project overview,
- business requirements,
- dataset distribution.

## Cells Visualizer
- average image visualization,
- variability analysis,
- image montage exploration.

## Mildew Detector
- image uploader,
- real-time prediction system,
- downloadable prediction reports.

## Project Hypothesis
- hypothesis explanation,
- validation conclusions.

## ML Performance
- training accuracy plots,
- training loss plots,
- interactive dataset distribution chart,
- model evaluation metrics.

---

# Model Performance

The final CNN model achieved:
- Training Accuracy: >99%
- Validation Accuracy: >99%
- Test Accuracy: 99.44%
- Stable validation loss
- Balanced prediction performance

The model successfully generalized to unseen test data.

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

| Feature | Expected Result | Status |
|---|---|---|
| Navigation Menu | All pages load correctly | PASS |
| Cells Visualizer | Visualizations display correctly | PASS |
| Image Montage | Random image samples are displayed correctly | PASS |
| Image Upload | Uploaded images generate predictions | PASS |
| Model Metrics | Training plots and interactive chart load correctly | PASS |

---

## Technical Validation

- Python code validated with PEP8 standards.
- Deployment tested in Heroku cloud environment.
- Model prediction pipeline verified successfully.
- Streamlit dashboard tested after deployment.
- Required image and output files verified in production.

---

# Deployment

## Heroku Deployment

The application was deployed using Heroku and Streamlit.

Deployment steps:
1. Create Heroku application.
2. Connect GitHub repository.
3. Configure Config Vars if required.
4. Deploy from the main branch.
5. Verify dashboard functionality after deployment.

---

# Repository and Branch Management

The project is maintained on a single stable deployment branch.

The deployed Heroku application uses the same branch as the final submitted GitHub repository to avoid branch inconsistencies and deployment path issues.

---

# Future Improvements

Possible future improvements for the project include:
- supporting additional cherry leaf diseases,
- implementing mobile device optimization,
- adding prediction confidence explanations,
- integrating cloud image storage,
- expanding the dataset with more real-world agricultural images,
- enabling batch image predictions for industrial use.

---

# Technologies Used

- Python
- TensorFlow / Keras
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- Jupyter Notebook

---

# Credits

- Dataset: Code Institute / Kaggle
- Streamlit Documentation
- TensorFlow Documentation
- Developed by Sorin Bivol