import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


def page_ml_performance_body():
    """
    Display the Machine Learning performance page.

    This page explains:
    - the dataset distribution,
    - the model training history,
    - the final test performance,
    - and an interactive chart required for dashboard interactivity.
    """

    version = "v1"
    outputs_path = Path("outputs") / version

    st.write("### Model Performance Metrics")

    st.info(
        "**Goal**: The model was trained to achieve a minimum accuracy of 97% "
        "on the test set. This page presents the dataset distribution, training "
        "history, and final model performance."
    )

    # -----------------------------
    # Section 1: Interactive Dataset Distribution
    # -----------------------------
    st.write("### Train, Validation and Test Set: Labels Frequencies")

    # Create a dataframe with the known dataset distribution
    labels_distribution_df = pd.DataFrame({
        "Set": [
            "Train", "Train",
            "Validation", "Validation",
            "Test", "Test"
        ],
        "Label": [
            "Healthy", "Powdery Mildew",
            "Healthy", "Powdery Mildew",
            "Healthy", "Powdery Mildew"
        ],
        "Count": [
            1472, 1472,
            211, 211,
            421, 421
        ]
    })

    # Display the distribution table
    st.dataframe(labels_distribution_df)

    # Create an interactive Plotly bar chart
    fig = px.bar(
        labels_distribution_df,
        x="Set",
        y="Count",
        color="Label",
        barmode="group",
        title="Interactive Dataset Distribution by Label"
    )

    # Render the interactive chart inside Streamlit
    st.plotly_chart(fig, use_container_width=True)

    st.write(
        "The dataset is balanced across all three subsets. Each subset contains "
        "the same number of healthy and powdery mildew images, which reduces the "
        "risk of class imbalance during model training."
    )

    st.write("---")

    # -----------------------------
    # Section 2: Model Training History
    # -----------------------------
    st.write("### Model Training History")

    col1, col2 = st.columns(2)

    acc_path = outputs_path / "model_training_acc.png"
    loss_path = outputs_path / "model_training_losses.png"

    # Display model accuracy plot if the file exists
    with col1:
        if acc_path.exists():
            st.image(
                str(acc_path),
                caption="Model Training Accuracy"
            )
        else:
            st.warning(
                "Accuracy plot not found. Please make sure "
                "model_training_acc.png exists inside outputs/v1."
            )

    # Display model loss plot if the file exists
    with col2:
        if loss_path.exists():
            st.image(
                str(loss_path),
                caption="Model Training Loss"
            )
        else:
            st.warning(
                "Loss plot not found. Please make sure "
                "model_training_losses.png exists inside outputs/v1."
            )

    st.success(
        "**Analysis**:\n\n"
        "- **Accuracy**: Training and validation accuracy reach very high values, "
        "showing that the model learned the main visual patterns of both classes.\n"
        "- **Loss**: The loss curves decrease during training, which indicates a "
        "stable learning process.\n"
        "- **Overfitting Check**: Validation performance remains close to training "
        "performance, suggesting that the model generalizes well to unseen data."
    )

    st.write("---")

    # -----------------------------
    # Section 3: Test Set Performance
    # -----------------------------
    st.write("### Generalised Performance on Test Set")

    performance_df = pd.DataFrame({
        "Metric": ["Loss", "Accuracy"],
        "Value": [0.0210, 0.9944]
    })

    st.table(performance_df)

    st.info(
        "The final accuracy on the unseen test set is **99.44%**. "
        "This exceeds the business requirement of at least 97% accuracy, "
        "therefore the model is suitable for supporting automated mildew "
        "detection in cherry leaves."
    )