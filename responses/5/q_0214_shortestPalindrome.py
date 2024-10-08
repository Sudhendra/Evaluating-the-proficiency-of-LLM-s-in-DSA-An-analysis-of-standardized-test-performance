class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        reverse = s[::-1]
        new_s = s + '#' + reverse
        prefix_suffix = [0] * len(new_s)

        for i in range(1, len(new_s)):
            j = prefix_suffix[i-1]
            while j > 0 and new_s[i] != new_s[j]:
                j = prefix_suffix[j-1]
            if new_s[i] == new_s[j]:
                j += 1
            prefix_suffix[i] = j

        return reverse[:len(s) - prefix_suffix[-1]] + s