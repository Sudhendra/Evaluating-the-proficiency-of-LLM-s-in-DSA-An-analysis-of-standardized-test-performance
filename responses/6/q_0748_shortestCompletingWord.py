from collections import Counter

class Solution:
    
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = ''.join(filter(str.isalpha, licensePlate.lower()))  # Remove digits and spaces, convert to lowercase
        licensePlate_counts = Counter(licensePlate)
        
        shortest_word = None
        shortest_length = float('inf')
        
        for word in words:
            word_counts = Counter(word)
            if all(word_counts[char] >= count for char, count in licensePlate_counts.items()):
                if shortest_word is None or len(word) < shortest_length:
                    shortest_word = word
                    shortest_length = len(word)
        
        return shortest_word
