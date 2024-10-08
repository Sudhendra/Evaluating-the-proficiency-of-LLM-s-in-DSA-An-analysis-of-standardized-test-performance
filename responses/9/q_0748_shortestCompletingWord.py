from collections import Counter
from typing import List

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target = Counter(letter.lower() for letter in licensePlate if letter.isalpha())
        shortest_word = None
        for word in words:
            if not shortest_word or len(word) < len(shortest_word):
                word_count = Counter(word)
                if all(word_count[letter] >= count for letter, count in target.items()):
                    shortest_word = word
        return shortest_word
