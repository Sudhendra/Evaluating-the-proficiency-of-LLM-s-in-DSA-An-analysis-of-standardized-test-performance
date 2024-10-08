class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = {}

        for path in paths:
            parts = path.split(' ')
            directory = parts[0]
            for i in range(1, len(parts)):
                file_info = parts[i].split('(')
                file_name = file_info[0]
                file_content = file_info[1][:-1]
                full_path = directory + '/' + file_name
                if file_content not in content_dict:
                    content_dict[file_content] = [full_path]
                else:
                    content_dict[file_content].append(full_path)

        duplicate_files = [files for files in content_dict.values() if len(files) > 1]
        
        return duplicate_files
