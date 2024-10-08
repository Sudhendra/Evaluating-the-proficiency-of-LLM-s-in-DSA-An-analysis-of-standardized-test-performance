from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        char_count = Counter(words[0])
        
        for word in words[1:]:
            word_count = Counter(word)
            for char in char_count:
                if char in word_count:
                    char_count[char] = min(char_count[char], word_count[char])
                else:
                    char_count[char] = 0
        
        for char, count in char_count.items():
            result.extend([char]*count)
        
        return result
