import os
import shutil
import random

def split_data(source_dir, train_dir, test_dir, valid_dir): 
    """
    Split data from source directory into train, test, and validation directories
    according to the specified split ratios.

    Args:
    - source_dir (str): Path to the source directory containing all the data.
    - train_dir (str): Path to the directory where training data will be copied.
    - test_dir (str): Path to the directory where testing data will be copied.
    - valid_dir (str): Path to the directory where validation data will be copied.
    - split_ratio (tuple): A tuple specifying the ratio of train, test, and validation data.
                           The values should sum up to 1.

    Returns:
    - None
    """

    # Create directories if they don't exist
    for directory in [train_dir, test_dir, valid_dir]:
        os.makedirs(directory, exist_ok=True)
        
    # Get all the files in the source directory
    files = os.listdir(source_dir)
    
    # Shuffle the files
    random.shuffle(files)
    
    # Split the files into train, test, and validation sets
    train_split_len = 700
    test_split_len = 200
    val_split_len = 100
    
    train_files = files[:train_split_len]
    test_files = files[train_split_len:train_split_len+test_split_len]
    val_files = files[train_split_len+test_split_len:]
    
    # Copy the files to the respective directories
    for file in train_files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(train_dir, file))
    for file in test_files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(test_dir, file))
    for file in val_files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(valid_dir, file))
    
    print("Data split successful")

# Set your source directory containing all the data
source_dir = "../../images/unidentify"

# Define paths for train, test, and validation directories
train_dir = "../../images/train/unidentify"
test_dir = "../../images/test/unidentify"
valid_dir = "../../images/valid/unidentify"

# Split data
split_data(source_dir, train_dir, test_dir, valid_dir)
