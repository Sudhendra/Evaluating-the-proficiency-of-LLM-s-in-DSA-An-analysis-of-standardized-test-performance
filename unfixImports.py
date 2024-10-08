import os
import re

def remove_added_imports(file_path):
    # List of added import statements for matching and removal
    added_import_statements = {
        'from typing import List',
        'from typing import Dict',
        'from typing import Set',
        'from typing import Tuple',
        'from typing import Optional',
        'from typing import Any',
        'from typing import Union',
        'from typing import Callable',
        'from typing import Mapping',
        'from typing import Sequence',
        'from typing import Iterable',
        'from typing import Iterator',
        'from typing import TypeVar',
        'from collections import deque as Deque',
        'from collections import Counter',
        'from collections import defaultdict as DefaultDict',
        'from typing import NamedTuple',
        'from typing import Coroutine',
        'from typing import Future',
        'from typing import AsyncIterator',
        'from typing import AsyncIterable',
        'from custom_module import ListNode',
        'from custom_module import TreeNode',
        'from data_structures import Point',
        # Add more as needed
    }

    # Read the file contents
    with open(file_path, 'r') as file:
        content = file.readlines()
    
    # Remove added imports if they exist in the file
    new_content = [line for line in content if line.strip() not in added_import_statements]
    
    # Write the updated content back to the file if changes were made
    if len(new_content) != len(content):
        with open(file_path, 'w') as file:
            file.writelines(new_content)
        print(f"Removed added imports from {file_path}")
    else:
        print(f"No added imports found in {file_path}")

def process_folder(folder_path):
    # Recursively walk through the directory tree
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.startswith('test_') and filename.endswith('.py'):
                file_path = os.path.join(root, filename)
                remove_added_imports(file_path)

# Define the directory
folder_path = '/home/mohit.y/chatGPT/responses'  # Update this path to your directory

# Perform the operation
process_folder(folder_path)
