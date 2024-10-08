from itertools import product

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def toggle_case(char):
            if char.isalpha():
                return char.lower() if char.isupper() else char.upper()
            return char

        results = []
        for letters in product(*[set([char.lower(), char.upper()]) if char.isalpha() else [char] for char in s]):
            result = ''.join(letters)
            results.append(result)
        
        return results
