class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit):
                stack.pop()
                k -= 1
            stack.append(digit)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        # Remove leading zeros
        while stack and stack[0] == '0':
            stack.pop(0)
        
        return '0' if not stack else ''.join(stack)
