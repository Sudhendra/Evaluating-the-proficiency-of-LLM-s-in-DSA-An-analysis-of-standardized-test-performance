from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_len = 0
        word_values = [0] * len(words)

        for i in range(len(words)):
            for char in words[i]:
                word_values[i] |= 1 << (ord(char) - ord('a'))

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if word_values[i] & word_values[j] == 0:
                    max_len = max(max_len, len(words[i]) * len(words[j]))

        return max_len
