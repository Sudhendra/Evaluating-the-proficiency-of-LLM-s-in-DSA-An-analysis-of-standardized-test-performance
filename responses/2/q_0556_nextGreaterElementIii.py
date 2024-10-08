class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        
        # Find the first decreasing digit from the right
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        
        if i == -1:
            return -1
        
        # Find the smallest digit to the right of i that is greater than digits[i]
        j = len(digits) - 1
        while j >= 0 and digits[j] <= digits[i]:
            j -= 1
        
        # Swap the two digits
        digits[i], digits[j] = digits[j], digits[i]
        
        # Reverse the digits to the right of i
        digits[i + 1:] = reversed(digits[i + 1:])
        
        result = int("".join(digits))
        
        return result if result <= 2**31 - 1 else -1