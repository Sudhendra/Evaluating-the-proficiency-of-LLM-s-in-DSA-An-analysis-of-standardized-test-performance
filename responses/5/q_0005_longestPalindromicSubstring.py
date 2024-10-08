class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        start = 0
        max_len = 1

        for i in range(1, len(s)):
            even = s[i - max_len - 1:i + 1]
            odd = s[i - max_len:i + 1]

            if i - max_len - 1 >= 0 and even == even[::-1]:
                start = i - max_len - 1
                max_len += 2
            elif i - max_len >= 0 and odd == odd[::-1]:
                start = i - max_len
                max_len += 1

        return s[start:start + max_len]

# Time complexity: O(n^2)
# Space complexity: O(1)