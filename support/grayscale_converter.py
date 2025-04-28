import os
from PIL import Image


def convert_images_to_grayscale(input_folder, output_folder):
    """
    Converts all images in the input folder to grayscale and saves them in the output folder.

    :param input_folder: Path to the folder containing the original images.
    :param output_folder: Path to the folder where grayscale images will be saved.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        # Check if the file is an image
        if os.path.isfile(input_path) and filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):
            try:
                # Open the image
                with Image.open(input_path) as img:
                    # Convert to grayscale
                    grayscale_img = img.convert("L")

                    # Save to the output folder
                    output_path = os.path.join(output_folder, filename)
                    grayscale_img.save(output_path)

                    print(f"Converted: {filename} -> {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
