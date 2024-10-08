class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit):
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # Remove remaining k digits from the end
        stack = stack[:-k] if k > 0 else stack
        
        # Remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        return result if result else '0'
