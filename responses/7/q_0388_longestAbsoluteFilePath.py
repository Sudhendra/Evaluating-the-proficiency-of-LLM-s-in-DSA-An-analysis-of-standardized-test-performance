class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        max_len = 0  # Initialize maximum length to 0
        path_dict = {0: 0}  # Initialize the root directory with length 0

        for line in input.split("\n"):
            name = line.lstrip("\t")
            level = len(line) - len(name)
            is_file = '.' in name

            path_dict[level] = path_dict[level - 1] + len(name) + 1 if is_file else path_dict[level - 1] + len(name)
            if is_file:
                max_len = max(max_len, path_dict[level])

        return max_len
