from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index, path, output):
            if index == len(digits):
                output.append(''.join(path))
                return
            
            for char in digit_map[digits[index]]:
                path.append(char)
                backtrack(index + 1, path, output)
                path.pop()
        
        output = []
        backtrack(0, [], output)
        
        return output