class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(rev[i:]):
                return rev[:i] + s
