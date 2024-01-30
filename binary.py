import cv2
import os

# Set threshold value
threshold_value = 0

# Path to directory containing images
directory_path = "/home/ytl0623/data/MI_proj2/data/OD/black/masks"
output_path = "/home/ytl0623/data/MI_proj2/data/OD/black/masks"

# Loop through each file in directory
for filename in os.listdir(directory_path):
    
    # Check if file is an image
    if filename.endswith(".png"):
        print(filename)
        # Read image using OpenCV
        image_path = os.path.join(directory_path, filename)
        image = cv2.imread(image_path)
        
        # Apply binary thresholding to image
        #binary_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
        
        # Save binary image to file
        binary_image_path = os.path.join(output_path, f"{filename}")
        cv2.imwrite(binary_image_path, binary_image)

