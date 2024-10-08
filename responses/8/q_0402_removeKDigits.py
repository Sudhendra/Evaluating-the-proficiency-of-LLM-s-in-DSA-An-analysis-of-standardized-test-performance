class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        num_to_remove = k
        
        for digit in num:
            while num_to_remove and stack and stack[-1] > digit:
                stack.pop()
                num_to_remove -= 1
            stack.append(digit)
        
        # Remove remaining numbers from the end
        stack = stack[:-num_to_remove] if num_to_remove else stack
        
        # Remove leading zeros
        return ''.join(stack).lstrip('0') or '0'
