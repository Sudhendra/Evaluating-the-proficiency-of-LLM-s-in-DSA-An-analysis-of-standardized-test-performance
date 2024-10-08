import os
import csv
import re
import sys
import subprocess
from tqdm import tqdm
from time import time

# Define the main directory where the test files are located across subfolders
main_directory = '/home/mohit.y/chatGPT/responses'

# Define the subfolder names
subfolders = os.listdir(main_directory)  # Automatically getting subfolders

for subfolder in subfolders:
    test_directory = os.path.join(main_directory, subfolder)

    # Get a list of all Python test files in the directory
    test_files = [file for file in os.listdir(test_directory) if file.startswith('test') and file.endswith('.py')]

    # Path to the CSV file to store the results in the corresponding subfolder
    csv_filename = os.path.join(test_directory, 'test_results.csv')
    csv_header = ['Test File', 'Passed', 'Failed', 'Errors']
    processed_files = set()

    # Check if CSV already exists to read processed files
    if os.path.exists(csv_filename):
        with open(csv_filename, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip the header
            processed_files = {rows[0] for rows in reader}

    with open(csv_filename, mode='a', newline='') as csvfile:  # Open file in append mode
        writer = csv.writer(csvfile)
        if not processed_files:  # Write header if the file was just created
            writer.writerow(csv_header)

        # Iterate over each test file using tqdm for a progress bar
        for test_file in tqdm(test_files, total=len(test_files), desc="Processing Test Files"):
            if test_file in processed_files:
                continue  # Skip this file as it's already processed

            # Build the command to run pytest
            command = ['pytest', '-q', os.path.join(test_directory, test_file)]
            
            try:
                # Start the timer and execute the command
                start_time = time()
                process = subprocess.run(command, text=True, capture_output=True, timeout=30)
                elapsed_time = time() - start_time
            except subprocess.TimeoutExpired:
                # If timeout, write an error code 100 in the error column
                writer.writerow([test_file, 0, 0, 100])
                print(f"Test {test_file} timed out and was terminated after 5 minutes.")
                continue

            # Capture the output from stdout
            output = process.stdout

            # Extract number of passed and failed tests using regex
            passed_matches = re.search(r'(\d+) passed', output)
            failed_matches = re.search(r'(\d+) failed', output)
            error_matches = re.search(r'(\d+) error', output)

            passed = int(passed_matches.group(1)) if passed_matches else 0
            failed = int(failed_matches.group(1)) if failed_matches else 0
            errors = int(error_matches.group(1)) if error_matches else 0  # Capture error count

            # Write the results to the CSV file
            writer.writerow([test_file, passed, failed, errors])

        print(f"Test results saved to: {csv_filename}")
