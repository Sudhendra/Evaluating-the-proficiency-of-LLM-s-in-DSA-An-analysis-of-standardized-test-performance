from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        unique_words = set(words)
        for word in words:
            for i in range(1, len(word)):
                unique_words.discard(word[i:])
        return sum(len(word) + 1 for word in unique_words)

# If you have multiple solutions, add them here as methods of the same class.
