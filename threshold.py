import cv2
import os

# Set threshold value
threshold_value = 0

# Path to directory containing images
directory_path = r"C:\Users\User\Downloads"
output_path = r"C:\Users\User\Downloads"

# Loop through each file in directory
for filename in os.listdir(directory_path):
    
    # Check if file is an image
    if filename.endswith(".jpg"):
        
        # Read image using OpenCV
        image_path = os.path.join(directory_path, filename)
        image = cv2.imread(image_path)
        
        # Apply binary thresholding to image
        _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
        
        # Save binary image to file
        binary_image_path = os.path.join(output_path, f"{filename}")
        cv2.imwrite(binary_image_path, binary_image)

