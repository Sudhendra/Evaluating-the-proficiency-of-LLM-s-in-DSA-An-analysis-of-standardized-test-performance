from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word, s):
            i = 0
            for char in word:
                i = s.find(char, i)
                if i == -1:
                    return False
                i += 1
            return True

        count = 0
        for word in words:
            if is_subsequence(word, s):
                count += 1
        return count