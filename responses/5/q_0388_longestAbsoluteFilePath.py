class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split('\n')
        stack = []
        max_len = 0
        
        for path in paths:
            depth = path.count('\t')
            while len(stack) > depth:
                stack.pop()
            
            if '.' in path:
                length = sum(len(item) for item in stack) + len(stack) + len(path) - depth
                max_len = max(max_len, length)
            else:
                stack.append(path.lstrip('\t'))
        
        return max_len
