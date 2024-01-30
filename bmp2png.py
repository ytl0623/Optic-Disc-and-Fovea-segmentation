import os
from PIL import Image

# Set the path to the directory containing BMP images
bmp_dir = r'C:\Users\User\Downloads\refuge_data\train\gts'

# Set the path to the directory where PNG images will be saved
png_dir = r'C:\Users\User\Downloads\refuge_data\train\gts\png'

# Loop through all BMP images in the directory
for filename in os.listdir(bmp_dir):
    if filename.endswith('.bmp'):
        # Open the BMP image
        bmp_image = Image.open(os.path.join(bmp_dir, filename))

        # Create the filename for the PNG image
        png_filename = os.path.splitext(filename)[0] + '.png'

        # Save the BMP image as a PNG image
        bmp_image.save(os.path.join(png_dir, png_filename), 'PNG')

        # Close the BMP image
        bmp_image.close()
