class Solution:
    
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ''
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_num, current_str))
                current_num = 0
                current_str = ''
            elif char.isalpha():
                current_str += char
            elif char == ']':
                num, prev_str = stack.pop()
                current_str = prev_str + num * current_str
        
        return current_str
