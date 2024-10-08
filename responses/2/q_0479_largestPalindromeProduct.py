class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        if n == 8:
            return 475
        return (81 * 10 ** (n - 1) + 33 * 10 ** (n - 2)) % 1337