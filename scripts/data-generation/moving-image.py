import os
import shutil
import random

def copy_images(src_dir, dest_dir, num_images):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Get a list of all image files in the source directory
    image_files = [file for file in os.listdir(src_dir) if file.endswith(('.jpg', '.jpeg', '.png'))]

    # Randomly select 'num_images' images from the source directory
    selected_images = random.sample(image_files, min(num_images, len(image_files)))

    # Copy selected images from source to destination directory
    for image_file in selected_images:
        src_path = os.path.join(src_dir, image_file)
        dest_path = os.path.join(dest_dir, image_file)
        shutil.copyfile(src_path, dest_path)
        print(f"Copied {image_file} to {dest_dir}")

src_dir = "../../images/unidentify"
dest_dir = "../../images/train/unidentify"
num_images = 1000  # Specify the number of images to copy
copy_images(src_dir, dest_dir, num_images)
