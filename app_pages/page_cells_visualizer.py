import streamlit as st
from pathlib import Path
from matplotlib.image import imread
import matplotlib.pyplot as plt
import random


def page_cells_visualizer_body():
    """Display the visual study page for healthy and mildew-infected cherry leaves."""

    st.write("### Cells Visualizer")

    st.info(
        "**Business Requirement 1**: The client is interested in conducting a visual study "
        "to differentiate a healthy cherry leaf from one affected by powdery mildew."
    )

    version = "v1"
    outputs_path = Path("outputs") / version
    data_dir = Path("inputs") / "test"

    if st.checkbox("Difference between average and variability image"):
        powdery_path = outputs_path / "avg_diff_powdery_mildew.png"
        healthy_path = outputs_path / "avg_diff_healthy.png"

        if powdery_path.exists() and healthy_path.exists():
            avg_powdery_mildew = imread(powdery_path)
            avg_healthy = imread(healthy_path)

            st.warning(
                "The visual study shows that powdery mildew leaves usually contain "
                "white cloudy patches, while healthy leaves appear clearer and greener."
            )

            st.image(
                avg_powdery_mildew,
                caption="Powdery Mildew - Average and Variability",
            )

            st.image(
                avg_healthy,
                caption="Healthy Leaf - Average and Variability",
            )

            st.write("---")
        else:
            st.error(
                "The average and variability images were not found. "
                "Please make sure the files exist inside the outputs/v1 folder."
            )

    if st.checkbox("Differences between average healthy and average powdery mildew leaves"):
        difference_path = outputs_path / "avg_diff.png"

        if difference_path.exists():
            diff_between_avgs = imread(difference_path)

            st.warning(
                "This study highlights the visual differences between healthy leaves "
                "and leaves affected by powdery mildew, including discoloration and "
                "texture changes."
            )

            st.image(
                diff_between_avgs,
                caption="Difference Between Average Images",
            )
        else:
            st.error(
                "The difference image was not found. "
                "Please make sure avg_diff.png exists inside the outputs/v1 folder."
            )

    if st.checkbox("Image Montage"):
        st.write(
            "To view the image montage, select a label and click the "
            "'Create Montage' button."
        )

        if data_dir.exists():
            labels = [
                folder.name
                for folder in data_dir.iterdir()
                if folder.is_dir()
            ]

            if labels:
                label_to_display = st.selectbox("Select label", labels)

                if st.button("Create Montage"):
                    create_montage(
                        dir_path=data_dir,
                        label_to_display=label_to_display,
                        nrows=3,
                        ncols=3,
                        figsize=(10, 10),
                    )
            else:
                st.error(
                    "No label folders were found inside inputs/test."
                )
        else:
            st.error(
                "The test image folder was not found. "
                "Please make sure inputs/test exists in the project."
            )


def create_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    """Generate and display a montage of random leaf images."""

    label_path = Path(dir_path) / label_to_display

    if not label_path.exists():
        st.error(f"The folder for label '{label_to_display}' was not found.")
        return

    images_list = [
        image
        for image in label_path.iterdir()
        if image.suffix.lower() in [".png", ".jpg", ".jpeg"]
    ]

    if len(images_list) < nrows * ncols:
        st.error("Not enough images in the folder to create a montage.")
        return

    selected_images = random.sample(images_list, nrows * ncols)

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    axes = axes.flatten()

    for index, image_path in enumerate(selected_images):
        image = imread(image_path)
        image_shape = image.shape

        axes[index].imshow(image)
        axes[index].set_title(
            f"W: {image_shape[1]}px | H: {image_shape[0]}px"
        )
        axes[index].axis("off")

    plt.tight_layout()
    st.pyplot(fig)