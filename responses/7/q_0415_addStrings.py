class Solution:
    
    def addStrings(self, num1: str, num2: str) -> str:
        # Pad the numbers with zeros on the left
        num1 = num1.zfill(max(len(num1), len(num2)))
        num2 = num2.zfill(max(len(num1), len(num2)))

        res = []
        carry = 0

        for i in range(len(num1) - 1, -1, -1):
            digit_sum = int(num1[i]) + int(num2[i]) + carry
            res.append(str(digit_sum % 10))
            carry = digit_sum // 10

        if carry:
            res.append(str(carry))

        return ''.join(res[::-1])
