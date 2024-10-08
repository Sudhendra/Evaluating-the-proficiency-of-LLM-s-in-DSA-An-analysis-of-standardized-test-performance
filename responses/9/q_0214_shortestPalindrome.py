class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        n = len(s)
        for i in range(n):
            if s[:n - i] == rev_s[i:]:
                return rev_s[:i] + s
        return ""
