from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        keypad = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        def backtrack(index, path):
            if index == len(digits):
                output.append("".join(path))
                return
            
            for char in keypad[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()
        
        output = []
        backtrack(0, [])
        return output
