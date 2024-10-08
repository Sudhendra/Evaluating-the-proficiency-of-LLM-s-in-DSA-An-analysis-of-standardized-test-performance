from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                file_info_parts = file_info.split('(')
                file_name = file_info_parts[0]
                content = file_info_parts[1][:-1]
                full_path = directory + '/' + file_name
                content_to_paths[content].append(full_path)
        
        duplicate_files = [paths for paths in content_to_paths.values() if len(paths) > 1]
        return duplicate_files
