from collections import Counter

class Solution:
    
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def isCompletingWord(word, licensePlate_count):
            word_count = Counter(word.lower())
            for char, count in licensePlate_count.items():
                if word_count[char] < count:
                    return False
            return True
        
        licensePlate = ''.join([ch.lower() for ch in licensePlate if ch.isalpha()])
        licensePlate_count = Counter(licensePlate)
        
        shortest_word = None
        shortest_length = float('inf')
        
        for word in words:
            if len(word) >= shortest_length:
                continue
                
            if isCompletingWord(word, licensePlate_count):
                shortest_word = word
                shortest_length = len(word)
        
        return shortest_word