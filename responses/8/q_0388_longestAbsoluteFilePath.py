class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split('\n')
        stack = [0]
        max_len = 0

        for path in paths:
            depth = path.count('\t')
            name = path.replace('\t', '')

            while depth + 1 < len(stack):
                stack.pop()

            if '.' in name:
                cur_len = stack[-1] + len(name)
                max_len = max(max_len, cur_len)
            else:
                stack.append(stack[-1] + len(name) + 1)

        return max_len
