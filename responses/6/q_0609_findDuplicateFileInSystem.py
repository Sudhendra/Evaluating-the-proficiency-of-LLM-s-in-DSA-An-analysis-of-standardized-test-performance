from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_path_map = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                file_name, content = file_info.split('(')
                content_path_map[content].append(directory + "/" + file_name)

        return [files for files in content_path_map.values() if len(files) > 1]
