class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        max_len = 0
        input = input.split('\n')
        for i in input:
            depth = i.count('\t')
            while len(stack) > depth:
                stack.pop()
            if '.' in i:
                length = sum(len(part) for part in stack) + len(stack) + len(i) - depth
                max_len = max(max_len, length)
            else:
                stack.append(i.replace('\t', ''))
        return max_len
