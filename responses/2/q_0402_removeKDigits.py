class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        keep = len(num) - k
        
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        result = ''.join(stack[:keep]).lstrip('0')
        return result if result else '0'