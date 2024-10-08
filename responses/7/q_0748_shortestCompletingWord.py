from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = "".join(filter(str.isalpha, licensePlate.lower()))
        licensePlate_counts = Counter(licensePlate)

        shortest_word = None
        shortest_length = float("inf")

        for word in words:
            word_counts = Counter(word)
            if all(licensePlate_counts[letter] <= word_counts[letter] for letter in licensePlate_counts):
                if len(word) < shortest_length:
                    shortest_word = word
                    shortest_length = len(word)

        return shortest_word
