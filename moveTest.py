import os
import shutil

def copy_test_files(source_dir, test_dir):
    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        # Check if the file starts with 'q_'
        if filename.startswith('q_') and filename.endswith('.py'):
            # Construct the corresponding test file name
            test_filename = 'test_' + filename

            # Build full paths for the test file in questions directory and the destination in the source directory
            test_file_path = os.path.join(test_dir, test_filename)
            target_file_path = os.path.join(source_dir, test_filename)

            # Check if the test file exists in the test directory
            if os.path.exists(test_file_path):
                # Copy the file to the source directory (same subfolder in responses)
                shutil.copy(test_file_path, target_file_path)
                print(f"Copied {test_filename} to {source_dir}")
            else:
                print(f"Test file {test_filename} does not exist in {test_dir}")

def process_all_folders(main_dir, questions_dir):
    # Iterate over each subfolder in the main directory
    for folder_name in os.listdir(main_dir):
        source_dir = os.path.join(main_dir, folder_name)

        # Check if the path is a directory
        if os.path.isdir(source_dir):
            # Perform the copying operation for each folder
            copy_test_files(source_dir, questions_dir)

# Define the directories
main_dir = '/home/mohit.y/chatGPT/responses'  # Path to the main directory containing subfolders
questions_dir = '/home/mohit.y/chatGPT/questions'  # Path to the directory containing test files

# Perform the copying operation for all folders
process_all_folders(main_dir, questions_dir)
