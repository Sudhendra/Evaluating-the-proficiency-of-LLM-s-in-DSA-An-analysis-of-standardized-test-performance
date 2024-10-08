from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def is_completing(word_counts, plate_counts):
            for char, count in plate_counts.items():
                if word_counts[char] < count:
                    return False
            return True
        
        licensePlate = ''.join(char.lower() for char in licensePlate if char.isalpha())
        licensePlate_counts = Counter(licensePlate)
        
        shortest_word = None
        for word in words:
            word = ''.join(char.lower() for char in word if char.isalpha())
            word_counts = Counter(word)
            if is_completing(word_counts, licensePlate_counts):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
                    
        return shortest_word