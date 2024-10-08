class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(s, L, a, modulus):
            n = len(s)
            h = 0
            for i in range(L):
                h = (h * a + ord(s[i])) % modulus
            seen = {h}
            aL = pow(a, L, modulus)
            for start in range(1, n - L + 1):
                h = (h * a - ord(s[start - 1]) * aL + ord(s[start + L - 1])) % modulus
                if h in seen:
                    return start
                seen.add(h)
            return -1

        def longest_repeated_substring(s):
            n = len(s)
            a = 26
            modulus = 2**63 - 1
            left, right = 1, n
            while left < right:
                L = left + (right - left) // 2
                if search(s, L, a, modulus) != -1:
                    left = L + 1
                else:
                    right = L
            start = search(s, left - 1, a, modulus)
            return s[start:start + left - 1]

        return longest_repeated_substring(s)
