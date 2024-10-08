# from leetscrape import GetQuestionsList, GetQuestion, GenerateCodeStub
# from tqdm import tqdm
# import logging

# # Setup basic logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# try:
#     ls = GetQuestionsList()
#     ls.scrape()  # Scrape the list of questions
# except Exception as e:
#     logging.error(f"Failed to scrape question list: {e}")
#     exit(1)  # Exit if we cannot retrieve the list of questions

# # Process each question
# for i in tqdm(range(len(ls.questions.titleSlug))):
#     title_slug = ls.questions.titleSlug[i]

#     try:
#         # Get the question body
#         fcs = GenerateCodeStub(titleSlug=title_slug)
#         fcs.generate(directory="/home/mohit.y/chatGPT/questions")
#     except FileNotFoundError as fnf_error:
#         logging.error(f"File not found error: {fnf_error} - Check directory path")
#     except PermissionError as perm_error:
#         logging.error(f"Permission error: {perm_error} - Check directory permissions")
#     except Exception as e:
#         logging.error(f"An error occurred while generating the code stub for '{title_slug}': {e}")


from leetscrape import GetQuestionsList, GenerateCodeStub
from tqdm import tqdm
import os
import logging
import fnmatch
# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    ls = GetQuestionsList()
    ls.scrape()  # Scrape the list of questions
except Exception as e:
    logging.error(f"Failed to scrape question list: {e}")
    exit(1)  # Exit if we cannot retrieve the list of questions

directory_path = "/home/mohit.y/chatGPT/questions"

# Check if directory exists to avoid FileNotFoundError in the loop
if not os.path.exists(directory_path):
    logging.error(f"Directory does not exist: {directory_path}")
    exit(1)

# Process each question
for i in tqdm(range(len(ls.questions))):
    qid = str(i).zfill(4)  # Assuming qid is accessible like this and needs zero padding
    title_slug = ls.questions.titleSlug[i]
    file_path_pattern = f'q_{qid}_*.py'
    file_exists = any(fnmatch.fnmatch(fname, file_path_pattern) for fname in os.listdir(directory_path))

    if not file_exists:
        try:
            # Get the question body
            fcs = GenerateCodeStub(titleSlug=title_slug)
            fcs.generate(directory=directory_path)
        except FileNotFoundError as fnf_error:
            logging.error(f"File not found error: {fnf_error} - Check directory path")
        except PermissionError as perm_error:
            logging.error(f"Permission error: {perm_error} - Check directory permissions")
        except Exception as e:
            logging.error(f"An error occurred while generating the code stub for '{title_slug}': {e}")
    else:
        logging.info(f"Code stub for QID {qid} already exists. Skipping generation.")
