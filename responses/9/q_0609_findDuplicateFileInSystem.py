from typing import List, Dict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict: Dict[str, List[str]] = {}

        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                file_parts = file_info.split("(")
                filename = file_parts[0]
                content = file_parts[1][:-1]

                full_path = directory + "/" + filename

                if content not in content_dict:
                    content_dict[content] = []

                content_dict[content].append(full_path)

        return [files for files in content_dict.values() if len(files) > 1]
