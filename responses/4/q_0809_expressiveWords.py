class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_stretchy(word):
            i, j, m, n = 0, 0, len(s), len(word)
            while i < m and j < n:
                if s[i] != word[j]:
                    return False
                start_i = i
                start_j = j
                while i < m and s[i] == s[start_i]:
                    i += 1
                while j < n and word[j] == word[start_j]:
                    j += 1
                if i - start_i < 3 and i - start_i != j - start_j:
                    return False
            if i == m and j == n:
                return True
            return False

        count = 0
        for word in words:
            if is_stretchy(word):
                count += 1
        return count
