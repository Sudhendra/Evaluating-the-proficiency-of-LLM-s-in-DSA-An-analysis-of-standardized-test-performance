class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split('\n')

        stack = []
        max_length = 0

        for path in paths:
            level = path.count('\t')
            while len(stack) > level:
                stack.pop()

            if '.' in path:
                length = len('/'.join(stack)) + len(path) - level
                max_length = max(max_length, length)
            else:
                stack.append(path.lstrip('\t'))

        return max_length
