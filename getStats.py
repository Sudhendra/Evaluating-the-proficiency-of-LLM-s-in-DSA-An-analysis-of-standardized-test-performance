import os
import csv
import pandas as pd

def strip_leading_zeros(qid):
    """ Helper function to remove leading zeros from the qid """
    return str(int(qid))

def process_results(main_directory, metadata_directory, target_directory):
    # Load the questions metadata from questions.csv
    questions_df = pd.read_csv(os.path.join(metadata_directory, 'questions.csv'))
    # Ensure QID in questions_df is string for consistency in merging
    questions_df['QID'] = questions_df['QID'].astype(str)

    # Traverse each subdirectory under the main directory
    for subfolder in os.listdir(main_directory):
        subfolder_path = os.path.join(main_directory, subfolder)
        if os.path.isdir(subfolder_path):
            results_path = os.path.join(subfolder_path, 'test_results.csv')
            if os.path.exists(results_path):
                # Read the test results into a DataFrame
                results_df = pd.read_csv(results_path)
                # Extract QIDs from file names, strip leading zeros and ensure it is string
                results_df['QID'] = results_df['Test File'].apply(lambda x: strip_leading_zeros(x.split('_')[2]))

                # Merge with the questions DataFrame
                merged_df = pd.merge(questions_df, results_df[['QID', 'Passed', 'Failed', 'Errors']], on='QID', how='inner')

                # Write the merged data to a new CSV file in the target directory, named after the subfolder
                output_path = os.path.join(target_directory, f'{subfolder}.csv')
                merged_df.to_csv(output_path, index=False)
                print(f"Merged data written to {output_path}")

# Define the paths
main_directory = '/home/mohit.y/chatGPT/responses'
metadata_directory = '/home/mohit.y/chatGPT/metadata'
target_directory = '/home/mohit.y/chatGPT/statistics'

# def merge_csv_based_on_qid(questions_csv_path, question_topics_csv_path, output_csv_path=None, merged=True):
#     if not merged:
#         # Load the CSV files into DataFrames
#         questions_df = pd.read_csv(questions_csv_path)
#         question_topics_df = pd.read_csv(question_topics_csv_path)
        
#         # Merge the DataFrames based on the 'QID' column
#         merged_df = pd.merge(questions_df, question_topics_df, on='QID', how='left')
        
#         # Print the merged DataFrame
#         print(merged_df)
        
#         # Optionally, write the merged DataFrame to a new CSV file
#         if output_csv_path:
#             merged_df.to_csv(output_csv_path, index=False)
#             print(f"Merged data written to {output_csv_path}")

# # Define the CSV paths
# questions_csv_path = '/home/mohit.y/chatGPT/metadata/questions.csv'
# question_topics_csv_path = '/home/mohit.y/chatGPT/metadata/questionTopics.csv'
# output_csv_path = '/home/mohit.y/chatGPT/metadata/questions.csv'

# # Merge the CSVs and write to a new file
# merge_csv_based_on_qid(questions_csv_path, question_topics_csv_path, output_csv_path, True)


# Process the results
process_results(main_directory, metadata_directory, target_directory)
