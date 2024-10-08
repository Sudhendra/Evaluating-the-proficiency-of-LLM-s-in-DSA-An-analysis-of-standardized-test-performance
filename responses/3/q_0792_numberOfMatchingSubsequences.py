from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word, s):
            i, j = 0, 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            return i == len(word)

        count = 0
        for word in words:
            if is_subsequence(word, s):
                count += 1
        return count