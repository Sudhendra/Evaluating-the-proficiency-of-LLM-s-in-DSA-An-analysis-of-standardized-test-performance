from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_stretchy(word: str) -> bool:
            i, j, n, m = 0, 0, len(s), len(word)
            for i in range(n):
                if j < m and s[i] == word[j]:
                    j += 1
                elif i > 0 and s[i] == s[i-1] and i+1 < n and s[i] != s[i+1]:
                    while j < m and word[j] == s[i]:
                        j += 1
                elif i > 1 and s[i] == s[i-1] and s[i-1] == s[i-2]:
                    continue
                else:
                    return False
            return j == m
        
        count = 0
        for word in words:
            if is_stretchy(word):
                count += 1
        return count