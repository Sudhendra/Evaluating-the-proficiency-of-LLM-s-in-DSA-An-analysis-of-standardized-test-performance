class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        rev_s = s[::-1]
        new_s = s + '#' + rev_s
        pi = [0] * len(new_s)

        for i in range(1, len(new_s)):
            j = pi[i - 1]

            while j > 0 and new_s[i] != new_s[j]:
                j = pi[j - 1]

            if new_s[i] == new_s[j]:
                j += 1

            pi[i] = j

        return rev_s[:len(s) - pi[-1]] + s
