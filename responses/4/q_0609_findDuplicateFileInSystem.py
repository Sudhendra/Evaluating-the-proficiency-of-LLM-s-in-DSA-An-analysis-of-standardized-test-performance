from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = defaultdict(list)
        
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                file, content = file_info.split('(')
                content_to_paths[content].append(directory + '/' + file)
        
        duplicates = [paths for paths in content_to_paths.values() if len(paths) > 1]
        
        return duplicates
