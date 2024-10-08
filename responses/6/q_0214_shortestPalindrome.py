class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev_s = s[::-1]
        for i in range(n):
            if s.startswith(rev_s[i:]):
                return rev_s[:i] + s
        return ""
