# Mildew Detection in Cherry Leaves

This is a Machine Learning project designed to detect powdery mildew in cherry leaves using computer vision. The system analyzes images of leaves and provides an instant diagnosis with high accuracy.

## Business Requirements
The project has been requested by 'Farmy & Foods', a company in the agricultural sector. The company is facing a challenge where their cherry plantations have been presenting powdery mildew, a fungal disease.

### Objectives:
1. **Visual Differentiation**: The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
2. **Instant Prediction**: The client is interested in predicting if a cherry tree is healthy or contains powdery mildew based on an image of a leaf.

## Project Hypotheses and Validation
* **Hypothesis**: Cherry leaves affected by powdery mildew can be visually identified by white, powdery-looking patches.
* **Validation**: The hypothesis was validated through an Exploratory Data Analysis (EDA) study and the training of a Convolutional Neural Network (CNN) which reached a high level of accuracy in identifying these patterns.

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
* It contains **4,208 images** of cherry leaves (healthy and mildew-infected).
* The images were split into:
    * **Train set**: Used to teach the model.
    * **Validation set**: Used to fine-tune the model during training.
    * **Test set**: Used to verify the final performance (99.4% accuracy).

## ML Business Logic
1. **Average Image & Variability Study**: Visualizes the "typical" look of each class.
2. **Difference between Averages**: Highlights the subtle differences between healthy and infected leaves.
3. **Image Montage**: Displays a random sample of images for quick visual inspection.
4. **CNN Model**: A deep learning model trained to classify leaves automatically.

## Dashboard Functional Features
The application is built using **Streamlit** and contains the following pages:

* **Project Summary**: Overview of the business requirements and dataset.
* **Cells Visualizer**: Visual study of the leaf categories (Average, Variability, and Montage).
* **Mildew Detector**: An interactive tool where users can upload leaf images for instant prediction.
* **Project Hypothesis**: Detailed explanation of the visual patterns identified.
* **ML Performance**: Technical metrics (Accuracy and Loss plots) showing the model's reliability.

## Deployment
### Local Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/Sori678/cherry-mildew-detector](https://github.com/Sori678/cherry-mildew-detector)
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Main Technologies Used
* **Python** (Core language)
* **TensorFlow/Keras** (Machine Learning model)
* **Streamlit** (Web Dashboard)
* **Pandas/NumPy** (Data Processing)
* **Matplotlib/Seaborn** (Visualization)

## Credits
* Dataset provided by Code Institute.
* Developed by [Your Name / Sori678].
```
