import os
import re

def add_missing_imports(file_path):
    # Define the commonly used types and their corresponding import statements
    types_to_imports = {
        'List': 'from typing import List',
        'Dict': 'from typing import Dict',
        'Set': 'from typing import Set',
        'Tuple': 'from typing import Tuple',
        'Optional': 'from typing import Optional',
        'Any': 'from typing import Any',
        'Union': 'from typing import Union',
        'Callable': 'from typing import Callable',
        'Mapping': 'from typing import Mapping',
        'Sequence': 'from typing import Sequence',
        'Iterable': 'from typing import Iterable',
        'Iterator': 'from typing import Iterator',
        'TypeVar': 'from typing import TypeVar',
        'Deque': 'from collections import deque as Deque',
        'Counter': 'from collections import Counter',
        'DefaultDict': 'from collections import defaultdict as DefaultDict',
        'NamedTuple': 'from typing import NamedTuple',
        'Coroutine': 'from typing import Coroutine',
        'Future': 'from typing import Future',
        'AsyncIterator': 'from typing import AsyncIterator',
        'AsyncIterable': 'from typing import AsyncIterable',
        'ListNode': 'from custom_module import ListNode',  # Example for custom type import
        'TreeNode': 'from custom_module import TreeNode',  # Another example for custom type
        'Point': 'from data_structures import Point',  # Hypothetical custom type
        # Add more custom or uncommon types as required
    }
    
    # Read the file contents
    with open(file_path, 'r') as file:
        content = file.readlines()
    
    existing_imports = set()
    needed_imports = set()

    # Check existing imports and detect needed imports
    for line in content:
        if line.startswith(('from ', 'import ')):
            existing_imports.add(line.strip())
        for type_name, import_statement in types_to_imports.items():
            if re.search(r'\b' + type_name + r'\b', line) and import_statement not in existing_imports:
                needed_imports.add(import_statement)
    
    # If there are missing imports, prepend them to the file
    if needed_imports:
        with open(file_path, 'w') as file:
            for imp in sorted(needed_imports):  # Sorting to maintain consistency
                file.write(imp + '\n')
            file.writelines(content)
        print(f"Added missing imports to {file_path}")
    else:
        print(f"No imports needed for {file_path}")

def process_folder(folder_path):
    # Recursively walk through the directory tree
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.startswith('test_') and filename.endswith('.py'):
                file_path = os.path.join(root, filename)
                add_missing_imports(file_path)

# Define the directory
folder_path = '/home/mohit.y/chatGPT/responses'  # Update this path to your directory

# Perform the operation
process_folder(folder_path)
