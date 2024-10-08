from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_set = set(words)
        for word in words:
            for i in range(1, len(word)):
                words_set.discard(word[i:])
        return sum(len(word) + 1 for word in words_set)

    def minimumLengthEncoding_alternative(self, words: List[str]) -> int:
        words.sort(key=lambda x: x[::-1])
        result = 0
        prev_word = ''
        for word in words:
            if not prev_word.endswith(word):
                result += len(word) + 1
            prev_word = word
        return result
