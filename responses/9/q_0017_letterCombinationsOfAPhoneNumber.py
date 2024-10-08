from typing import List

class Solution:
    
    digit_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return
            
            letters = self.digit_to_letters[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        if not digits:
            return []
        
        combinations = []
        backtrack(0, [])
        return combinations
