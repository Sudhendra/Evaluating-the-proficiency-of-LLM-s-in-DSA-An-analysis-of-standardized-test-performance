import os

def process_files_in_folder(folder_path):
    # List all files in the current folder
    for file_name in os.listdir(folder_path):
        # Construct full file path
        file_path = os.path.join(folder_path, file_name)
        # Check if it's a Python file starting with 'q_'
        if file_name.startswith('q_') and file_name.endswith('.py'):
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Check if the first and last lines contain triple quotes
            if lines and lines[0].strip().startswith('```') and lines[-1].strip().endswith('```'):
                # Remove the first and last lines
                lines = lines[1:-1]
            
            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.writelines(lines)

def process_all_folders(main_folder):
    # Iterate over each subfolder in the main folder
    for folder_name in os.listdir(main_folder):
        subfolder_path = os.path.join(main_folder, folder_name)
        # Check if the path is indeed a directory
        if os.path.isdir(subfolder_path):
            # Process files in the current subfolder
            process_files_in_folder(subfolder_path)

# Main folder path
main_folder = '/home/mohit.y/chatGPT/responses'

# Process all folders
process_all_folders(main_folder)
