class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(rev_s[i:]):
                return rev_s[:i] + s