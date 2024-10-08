from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(s, index, current, result):
            if index == len(s):
                result.append(current)
                return
            if s[index].isalpha():
                backtrack(s, index + 1, current + s[index].lower(), result)
                backtrack(s, index + 1, current + s[index].upper(), result)
            else:
                backtrack(s, index + 1, current + s[index], result)
        
        result = []
        backtrack(s, 0, "", result)
        return result
