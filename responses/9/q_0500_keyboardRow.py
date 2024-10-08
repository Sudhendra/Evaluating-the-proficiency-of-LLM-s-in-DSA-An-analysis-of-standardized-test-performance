from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        
        for word in words:
            for row in keyboard_rows:
                if all(char.lower() in row for char in word):
                    result.append(word)
                    break
        
        return result
