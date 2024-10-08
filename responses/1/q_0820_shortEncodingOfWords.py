from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        for word in words:
            for i in range(1, len(word)):
                if word[i:] in words:
                    words.discard(word[i:])
        return sum(len(word) + 1 for word in words)
