from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word, s):
            i = 0
            for char in word:
                if i >= len(s):
                    return False
                while s[i] != char:
                    i += 1
                    if i >= len(s):
                        return False
                i += 1
            return True

        count = 0
        for word in words:
            if is_subsequence(word, s):
                count += 1
        return count
