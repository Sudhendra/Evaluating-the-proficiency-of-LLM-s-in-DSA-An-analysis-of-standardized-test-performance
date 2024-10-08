class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        max_len = 0
        input_lines = input.split('\n')
        
        for line in input_lines:
            depth = line.count('\t')
            name = line.replace('\t', '')
            
            while len(stack) > depth:
                stack.pop()
            
            if '.' in name:
                curr_len = sum(len(s) for s in stack) + len(stack) + len(name)
                max_len = max(max_len, curr_len)
            else:
                stack.append(name)
        
        return max_len