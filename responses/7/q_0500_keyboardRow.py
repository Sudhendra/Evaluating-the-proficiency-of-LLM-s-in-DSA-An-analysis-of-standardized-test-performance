from typing import List

class Solution:
    
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        result = []
        
        for word in words:
            word_set = set(word.lower())
            
            if word_set.issubset(first_row) or word_set.issubset(second_row) or word_set.issubset(third_row):
                result.append(word)
        
        return result
