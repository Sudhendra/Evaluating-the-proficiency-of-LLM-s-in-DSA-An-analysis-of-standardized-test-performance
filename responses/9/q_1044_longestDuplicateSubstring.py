class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(left, right, n, s, a, modulus):
            h = 0
            for i in range(left, right):
                h = (h * a + ord(s[i])) % modulus
            seen = {h}
            aL = pow(a, n, modulus)
            for start in range(1, len(s) - n + 1):
                h = (h * a - ord(s[start - 1]) * aL + ord(s[start + n - 1])) % modulus
                if h in seen:
                    return start
                seen.add(h)
            return -1

        def longestDup(s):
            n = len(s)
            a = 26
            modulus = 2**63 - 1
            left, right = 1, n
            result = ""
            while left <= right:
                mid = (left + right) // 2
                start = search(mid, n, s, a, modulus)
                if start != -1:
                    result = s[start:start + mid]
                    left = mid + 1
                else:
                    right = mid - 1
            return result

        return longestDup(s)
