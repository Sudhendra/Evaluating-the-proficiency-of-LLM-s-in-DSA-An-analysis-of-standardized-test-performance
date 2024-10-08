class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ''
        
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                stack.append((curr_num, curr_str))
                curr_num = 0
                curr_str = ''
            elif char == ']':
                num, prev_str = stack.pop()
                curr_str = prev_str + num * curr_str
            else:
                curr_str += char
        
        return curr_str
