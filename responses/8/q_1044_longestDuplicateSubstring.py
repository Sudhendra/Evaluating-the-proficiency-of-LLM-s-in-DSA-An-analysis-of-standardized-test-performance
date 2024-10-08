class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(s, l, modulo):
            n = len(s)
            h = 0
            a = 26
            for i in range(l):
                h = (h * a + ord(s[i]) - ord('a')) % modulo
            seen = {h}
            aL = pow(a, l, modulo)  # a^l % modulo
            for start in range(1, n - l + 1):
                h = (h * a - aL * (ord(s[start - 1]) - ord('a')) + (ord(s[start + l - 1]) - ord('a'))) % modulo
                if h in seen:
                    return start
                seen.add(h)
            return -1

        def searchForLength(s, l):
            base = 26
            modulo = 2 ** 63 - 1
            pos = search(s, l, modulo)
            if pos != -1:
                return s[pos: pos + l]
            return ""

        n = len(s)
        left, right = 1, n
        result = ""
        while left <= right:
            mid = left + (right - left) // 2
            substr = searchForLength(s, mid)
            if substr:
                if len(substr) > len(result):
                    result = substr
                left = mid + 1
            else:
                right = mid - 1
        return result
