class Solution:
    
    def lengthLongestPath(self, input: str) -> int:
        stack = [-1]
        max_len = 0
        for s in input.split('\n'):
            depth = s.count('\t')
            while depth + 1 < len(stack):
                stack.pop()
            length = len(s.replace('\t', ''))
            if '.' in s:
                max_len = max(max_len, stack[-1] + length + 1)
            else:
                stack.append(stack[-1] + length + 1)
        return max_len
