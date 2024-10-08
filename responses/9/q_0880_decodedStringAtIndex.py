class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = []
        curr_str = ""
        
        for char in s:
            if char.isalpha():
                curr_str += char
            else:
                stack.append((curr_str, int(char)))
                curr_str = ""
        
        for i in range(len(stack) - 1, -1, -1):
            curr_str, repeat = stack[i]
            k %= len(curr_str) * repeat
            
            if k == 0 and char.isalpha():
                return char
        
        return curr_str[k-1]
