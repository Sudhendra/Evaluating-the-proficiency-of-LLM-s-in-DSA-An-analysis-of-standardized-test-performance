from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_files = defaultdict(list)

        for path in paths:
            directory, *files = path.split(' ')
            for file in files:
                file_name, content = file.split('(')
                content_to_files[content].append(directory + '/' + file_name)

        return [files for files in content_to_files.values() if len(files) > 1]
