# import os

# def rename_images(folder_path, prefix="a_"):
#     images = sorted(os.listdir(folder_path))
#     image_no = 1

#     for file_name in images:
#         file_path = os.path.join(folder_path, file_name)
        
#         # Skip non-image files
#         if not file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
#             continue
        
#         # Extract file extension
#         file_ext = os.path.splitext(file_name)[1]
        
#         # Create new file name
#         new_file_name = f"{prefix}{image_no}{file_ext}"
#         new_file_path = os.path.join(folder_path, new_file_name)
        
#         # Rename the file
#         os.rename(file_path, new_file_path)
#         print(f"Renamed: {file_name} -> {new_file_name}")
#         image_no += 1

# # Example usage
# folder_path = "./dataset_scanned/digits_dataset"
# rename_images(folder_path,"digit_")



# import os
# from PIL import Image, ImageOps
# import numpy as np

# def ensure_white_background_black_symbols(input_folder, output_folder):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     for file_name in os.listdir(input_folder):
#         input_path = os.path.join(input_folder, file_name)
        
#         # Skip non-image files
#         if not file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
#             continue
        
#         with Image.open(input_path) as img:
#             # Convert to grayscale
#             img = img.convert("L")
            
#             # Calculate the average pixel intensity
#             avg_pixel = np.array(img).mean()
            
#             # If the image has a dark background (avg closer to black), invert it
#             if avg_pixel < 128:  # 0 is black, 255 is white
#                 img = ImageOps.invert(img)
            
#             # Save the corrected image
#             output_path = os.path.join(output_folder, file_name)
#             img.save(output_path)
#             print(f"Processed and saved: {output_path}")

# # Example usage
# input_folder = "./dataset_scanned/sharp"
# output_folder = "./dataset_scanned/sharp_inverted"
# ensure_white_background_black_symbols(input_folder, output_folder)

# import os
# from PIL import Image, ImageOps

# def invert_binary_images_in_folder(input_folder, output_folder):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     for file_name in os.listdir(input_folder):
#         input_path = os.path.join(input_folder, file_name)
        
#         # Skip non-image files
#         if not file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
#             continue
        
#         with Image.open(input_path) as img:
#             # Ensure the image is in grayscale
#             img = img.convert("L")
            
#             # Invert the image
#             inverted_image = ImageOps.invert(img)
            
#             # Save the inverted image
#             output_path = os.path.join(output_folder, file_name)
#             inverted_image.save(output_path)
#             print(f"Saved: {output_path}")

# # Example usage
# input_folder = "./dataset_scanned/digits_dataset"
# output_folder = "./dataset_scanned/digits_dataset_inverted"
# invert_binary_images_in_folder(input_folder, output_folder)

import os
from PIL import Image

def rename_and_convert_images(folder_path):
    # Get all files in the folder
    files = os.listdir(folder_path)
    
    # Filter image files and sort them
    image_files = [f for f in files if f.lower().endswith(('.png', '.bmp', '.jpg', '.jpeg'))]
    image_files.sort()  # Optional: Ensures renaming follows sorted order

    # Process each image
    for idx, file_name in enumerate(image_files, start=1):
        old_path = os.path.join(folder_path, file_name)
        
        # Set new name with index and PNG extension
        new_name = f"{idx}.png"
        new_path = os.path.join(folder_path, new_name)
        
        # Convert BMP to PNG if necessary
        if file_name.lower().endswith('.bmp'):
            with Image.open(old_path) as img:
                img.save(new_path, "PNG")  # Convert to PNG
            os.remove(old_path)  # Remove the old BMP file
        else:
            os.rename(old_path, new_path)  # Rename other image files

    print("Renaming and conversion completed.")

# Provide the folder path containing the images
folder_path = "./dataset_scanned/natural"
rename_and_convert_images(folder_path)