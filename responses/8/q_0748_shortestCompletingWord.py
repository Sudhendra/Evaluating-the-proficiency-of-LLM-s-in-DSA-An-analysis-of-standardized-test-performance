from collections import Counter

class Solution:
    def isCompletingWord(self, word: str, plate_count: Counter) -> bool:
        word_count = Counter(word.lower())
        for char, count in plate_count.items():
            if word_count[char] < count:
                return False
        return True

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate_count = Counter(char.lower() for char in licensePlate if char.isalpha())
        shortest_word = None
        for word in words:
            if self.isCompletingWord(word, plate_count):
                if not shortest_word or len(word) < len(shortest_word):
                    shortest_word = word
        return shortest_word
