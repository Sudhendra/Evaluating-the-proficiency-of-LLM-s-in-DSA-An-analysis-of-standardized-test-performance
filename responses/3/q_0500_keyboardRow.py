from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        
        for word in words:
            in_one_row = True
            first_char = word[0].lower()
            if first_char in rows[0]:
                row = 0
            elif first_char in rows[1]:
                row = 1
            else:
                row = 2
                
            for char in word[1:]:
                if char.lower() not in rows[row]:
                    in_one_row = False
                    break
                    
            if in_one_row:
                result.append(word)
                
        return result
