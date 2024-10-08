class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        
        while i >= 0 or j >= 0 or carry:
            digit_sum = carry
            if i >= 0:
                digit_sum += int(num1[i])
                i -= 1
            if j >= 0:
                digit_sum += int(num2[j])
                j -= 1
            
            carry = digit_sum // 10
            result.append(str(digit_sum % 10))
        
        return ''.join(result[::-1])
