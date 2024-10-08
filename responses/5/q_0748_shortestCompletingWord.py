from collections import Counter
from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def count_chars(s):
            count = Counter(c.lower() for c in s if c.isalpha())
            return count

        target_count = count_chars(licensePlate)
        shortest_word = None

        for word in words:
            word_count = count_chars(word)
            if all(word_count[char] >= target_count[char] for char in target_count):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word

        return shortest_word
