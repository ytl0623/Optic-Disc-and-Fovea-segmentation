import os
import cv2
from PIL import Image

png_dir = r'C:\Users\User\Downloads\refuge_data\train\gts\png'

# Set the path to the directory where PNG images will be saved
invert_dir = r'C:\Users\User\Downloads\refuge_data\train\gts\invert'

for filename in os.listdir(png_dir):
    if filename.endswith('.png'):
        image = cv2.imread(os.path.join(png_dir, filename))
        image = ~image
        cv2.imwrite(os.path.join(invert_dir, filename),image)