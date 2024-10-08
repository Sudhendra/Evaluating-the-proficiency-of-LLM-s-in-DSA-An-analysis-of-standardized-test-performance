class Solution:
    def nearestPalindromic(self, n: str) -> str:
        n = int(n)
        small_palindrome = large_palindrome = self.find_palindrome(n)

        while small_palindrome == large_palindrome:
            small_palindrome = self.find_palindrome(n - 1)
            large_palindrome = self.find_palindrome(n + 1)
            n -= 1

        if abs(int(n - small_palindrome)) <= abs(int(n + 1 - large_palindrome)):
            return str(small_palindrome)
        else:
            return str(large_palindrome)

    def find_palindrome(self, x: int) -> int:
        while True:
            if str(x) == str(x)[::-1]:
                return x
            x += 1
