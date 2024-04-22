
---

# Image Cropping and Bounding Box Detection

This Python script utilizes the `PIL` (Python Imaging Library) and `matplotlib` libraries to perform image processing tasks such as cropping and bounding box detection on medical images. The script loads a CT image, rotates it, detects non-zero pixels, finds the bounding box coordinates, and crops the image accordingly. Finally, it displays the cropped images using `matplotlib`.

## Prerequisites

Ensure you have the following Python libraries installed:

- PIL (Python Imaging Library)
- matplotlib
- numpy

## Usage

1. **Image Preparation**:
   - Provide the path to your CT image (`ct_image.png`) in the script.
   - Optionally, adjust the rotation angle or other image processing parameters as needed.

2. **Run the Script**:
   - Execute the script to perform image cropping and bounding box detection.
   - The script will display the cropped images using `matplotlib`.

## Customization

- **Image Processing Parameters**: Modify the image processing logic, such as rotation angle or cropping dimensions, to suit your specific requirements.
- **Display Settings**: Customize the display settings of the cropped images, such as colormap and axis visibility, using `matplotlib` functions.

## Note

- Ensure your CT image file (`ct_image.png`) is accessible and correctly referenced in the script.
- Customize the script according to your specific image processing needs and preferences.

---

