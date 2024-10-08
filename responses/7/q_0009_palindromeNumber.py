class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse_number = 0
        while x > reverse_number:
            reverse_number = reverse_number * 10 + x % 10
            x //= 10
        return x == reverse_number or x == reverse_number // 10
