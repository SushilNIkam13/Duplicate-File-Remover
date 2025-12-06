from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import hashlib
from pathlib import Path


def calculate_hash(file_name):
    # Calculates the MD5 hash of the file
    with open(file_name, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def is_file(file_name):
    # Checks if the file exists
    return Path(file_name).is_file()


def delete_duplicate_files(path):
    # Create a dictionary to store unique file hashes and their corresponding file names
    unique = {}
    
    # Get a list of all the files in the specified directory
    files_list = [os.path.join(path, file) for file in os.listdir(path)]
    
    # Iterate over each file in the directory
    for file_name in files_list:
        # Check if the current file is a valid file
        if is_file(file_name):
            # Calculate the hash of the file
            file_hash = calculate_hash(file_name)
            
            # Check if the hash is already in the dictionary
            if file_hash not in unique:
                # If it's not in the dictionary, add it to the dictionary
                unique[file_hash] = file_name
            else:
                # If it's already in the dictionary, delete the duplicate file
                print(f"Deleting duplicate file: {file_name}")
                os.remove(file_name)


if __name__ == '__main__':
    # Use Tkinter to open a file dialog box for the user to select a directory
    Tk().withdraw()
    path = askdirectory(title='Select Folder')
    
    # Check if the specified path exists
    if not os.path.exists(path):
        raise Exception("Path does not exist")
    
    # Call the delete_duplicate_files function to remove any duplicate files
    delete_duplicate_files(path)
