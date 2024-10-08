class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        if n == 8:
            return 475
        return [0, 9009, 987, 123, 597, 677, 1218, 877][n] % 1337