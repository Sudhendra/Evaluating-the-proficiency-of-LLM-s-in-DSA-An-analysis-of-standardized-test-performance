class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            sum_digit = digits[i] + carry
            digits[i] = sum_digit % 10
            carry = sum_digit // 10
        if carry > 0:
            digits.insert(0, carry)
        return digits