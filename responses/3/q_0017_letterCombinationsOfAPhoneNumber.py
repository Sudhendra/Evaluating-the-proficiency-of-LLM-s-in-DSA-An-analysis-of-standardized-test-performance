from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        def backtrack(combination, next_digits):
            if not next_digits:
                result.append(combination)
            else:
                for letter in digit_to_letters[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        result = []
        backtrack('', digits)
        return result
