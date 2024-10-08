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
        
        n = len(s)
        a = 26
        modulus = 2**63 - 1
        left, right = 1, n
        result = ""
        while left <= right:
            L = left + (right - left) // 2
            start = search(s, L, a, modulus)
            if start != -1:
                result = s[start:start + L]
                left = L + 1
            else:
                right = L - 1
        return result
