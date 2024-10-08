from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_stretchy(word: str) -> bool:
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] != word[j]:
                    return False
                start_i = i
                start_j = j
                while i < len(s) and s[i] == s[start_i]:
                    i += 1
                while j < len(word) and word[j] == word[start_j]:
                    j += 1
                if i - start_i < j - start_j or (i - start_i < 3 and i - start_i != j - start_j):
                    return False
            return i == len(s) and j == len(word)

        count = 0
        for word in words:
            if is_stretchy(word):
                count += 1
        return count
