from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        
        for word in words:
            word_lower = word.lower()
            if all(any(ch in row for row in rows) for ch in word_lower):
                result.append(word)
        
        return result
