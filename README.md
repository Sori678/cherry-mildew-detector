# Mildew Detection in Cherry Leaves

This is a Machine Learning project designed to detect powdery mildew in cherry leaves using computer vision. The system analyzes images of leaves and provides an instant diagnosis with high accuracy, helping farmers automate disease detection.

## Business Requirements
The project has been requested by 'Farmy & Foods', a company in the agricultural sector. The company is facing a challenge where their cherry plantations have been presenting powdery mildew, a fungal disease.

### Objectives:
1. **Visual Differentiation**: Conduct a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
2. **Instant Prediction**: Predict if a cherry tree is healthy or contains powdery mildew based on an image of a leaf.

---

## User Stories (Agile Methodology)

The project was developed using Agile principles. Tasks were managed via a GitHub Kanban board to ensure transparency and iterative progress.

| User Story ID | User Story Description | Business Requirement | Status |
|---------------|------------------------|-----------------------|--------|
| US_01 | As a user, I want to navigate easily through a dashboard to view the project summary and dataset info. | BR_01, BR_02 | Done |
| US_02 | As a user, I want to see the visual differences between healthy and mildew-infected leaves (average and variability). | BR_01 | Done |
| US_03 | As a user, I want to see a montage of leaf samples to understand the visual patterns. | BR_01 | Done |
| US_04 | As a user, I want to upload leaf images and get an instant prediction report. | BR_02 | Done |
| US_05 | As a user, I want to see the model performance metrics to trust the system's accuracy. | BR_02 | Done |

---

## Project Hypotheses and Validation
* **Hypothesis**: Cherry leaves affected by powdery mildew can be visually identified by white, powdery-looking patches or distinct discolorations.
* **Validation**: The hypothesis was validated through Exploratory Data Analysis (EDA) comparing mean images and variability. The CNN model reached an accuracy of **99.4%** on the test set, confirming that these visual patterns are highly distinguishable.

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
* It contains **4,208 images** of cherry leaves.
* **Train set**: 2,944 images.
* **Validation set**: 422 images.
* **Test set**: 842 images.

## ML Business Logic
1. **Average Image & Variability Study**: Visualizes the mathematical mean of each category to spot common traits.
2. **Difference between Averages**: Highlights contrast between healthy and infected leaves.
3. **Image Montage**: Provides random sampling for manual verification.
4. **CNN Model**: A Convolutional Neural Network architecture designed for binary classification (Healthy vs. Mildew).

---

## Dashboard Functional Features
The application is built using **Streamlit** and contains:

* **Project Summary**: Quick look at objectives and dataset stats.
* **Cells Visualizer**: Interactive toggles for Average, Variability, and Montages.
* **Mildew Detector**: File uploader (PNG/JPG) with real-time prediction and a downloadable CSV report.
* **Project Hypothesis**: Deep dive into the "why" behind the model's decisions.
* **ML Performance**: Technical graphs for Accuracy/Loss and Confusion Matrix.

---

## Testing

### Manual Testing
| Page | Feature | Action | Expected Result | Status |
|------|---------|--------|-----------------|--------|
| Navigation | Sidebar | Click on 'Mildew Detector' | Page content updates immediately | Pass |
| Visualizer | Checkboxes | Toggle 'Difference between Averages' | Displays the specific comparison image | Pass |
| Detector | File Uploader | Upload 3 sample images | Predictions appear for each image | Pass |
| Detector | Table Report | View the summary table | All uploaded filenames and results are listed | Pass |

### Technical Validation
* **Python**: Code passed PEP8 linting (no critical errors).
* **Environment**: Tested in a virtual environment to ensure dependency stability.
* **Deployment**: Verified live on Heroku (Cloud).

---

## Fixed Bugs
1. **Issue**: `FileNotFoundError` for the model on Heroku.
   * **Fix**: Implemented `os.path.join(os.getcwd(), ...)` to ensure absolute paths on the server.
2. **Issue**: Deployment failed due to slug size (500MB+).
   * **Fix**: Replaced `tensorflow` with `tensorflow-cpu` in `requirements.txt` to minimize footprint.
3. **Issue**: Streamlit layout breaking on mobile.
   * **Fix**: Adjusted image resizing to be responsive within the Streamlit container.

---

## Deployment
### Local Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/Sori678/cherry-mildew-detector](https://github.com/Sori678/cherry-mildew-detector)
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Or venv\Scripts\activate on Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   streamlit run app.py
## Main Technologies Used
Python

* TensorFlow/Keras

* Streamlit

* Pandas / NumPy

* Matplotlib / Seaborn

* Scikit-learn

## Credits
* Dataset: Code Institute / Kaggle.

* Support: Mentor sessions and peer reviews.

* Developed by Bivol Sorin / Sori678.