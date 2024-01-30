from PIL import Image
import os

# Set the input directory
input_dir = r"C:\Users\User\Downloads\idrid_masks"

# Set the output directory
output_dir = r"C:\Users\User\Downloads\idrid_masks"

# Iterate over all the TIF files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".tif"):
        # Open the TIF file using PIL
        tif_image = Image.open(os.path.join(input_dir, filename))
        
        # Convert the TIF image to PNG format
        png_image = tif_image.convert("RGBA")
        
        # Save the PNG image to the output directory
        png_image.save(os.path.join(output_dir, filename.replace(".tif", ".png")))
