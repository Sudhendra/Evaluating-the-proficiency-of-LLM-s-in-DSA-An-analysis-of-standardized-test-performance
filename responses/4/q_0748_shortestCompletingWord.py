from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def is_completing_word(word: str, plate_letters: Counter) -> bool:
            word_letters = Counter([char.lower() for char in word if char.isalpha()])
            for letter, count in plate_letters.items():
                if word_letters[letter] < count:
                    return False
            return True
        
        licensePlate_letters = Counter([char.lower() for char in licensePlate if char.isalpha()])
        
        shortest_word = None
        for word in words:
            if (shortest_word is None or len(word) < len(shortest_word)) and is_completing_word(word, licensePlate_letters):
                shortest_word = word
                
        return shortest_word
