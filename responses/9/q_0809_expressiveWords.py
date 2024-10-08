from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_stretchy(word):
            i, j, n, m = 0, 0, len(s), len(word)
            for i in range(n):
                if j < m and s[i] == word[j]:
                    j += 1
                elif i > 0 and s[i - 1] == s[i] and i + 1 < n and s[i] == s[i + 1]:
                    continue
                elif i > 1 and s[i - 2] == s[i - 1] and s[i - 1] == s[i]:
                    continue
                else:
                    return False
            return j == m

        return sum(is_stretchy(word) for word in words)
