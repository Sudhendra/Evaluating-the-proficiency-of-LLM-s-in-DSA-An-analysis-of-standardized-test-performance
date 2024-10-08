class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i+1]:
            i -= 1
        
        if i == -1:
            return -1
        
        j = len(digits) - 1
        while j >= 0 and digits[j] <= digits[i]:
            j -= 1
        
        digits[i], digits[j] = digits[j], digits[i]
        digits[i+1:] = digits[i+1:][::-1]
        
        result = int(''.join(digits))
        
        if result > 2**31 - 1:
            return -1
        else:
            return result