class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_stretchy(word):
            i, j, n, m = 0, 0, len(s), len(word)
            while i < n and j < m:
                if s[i] != word[j]:
                    return False
                ch = s[i]
                len_s = 0
                len_w = 0
                while i < n and s[i] == ch:
                    i += 1
                    len_s += 1
                while j < m and word[j] == ch:
                    j += 1
                    len_w += 1
                if len_s < 3 and len_s != len_w:
                    return False
                if len_s < len_w:
                    return False
            return i == n and j == m

        count = 0
        for word in words:
            if is_stretchy(word):
                count += 1
        return count