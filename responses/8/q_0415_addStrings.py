class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                digit1 = ord(num1[i]) - ord('0')
            else:
                digit1 = 0
            
            if j >= 0:
                digit2 = ord(num2[j]) - ord('0')
            else:
                digit2 = 0
            
            current_sum = digit1 + digit2 + carry
            carry = current_sum // 10
            result.append(str(current_sum % 10))
            
            i -= 1
            j -= 1
        
        return ''.join(result[::-1])
