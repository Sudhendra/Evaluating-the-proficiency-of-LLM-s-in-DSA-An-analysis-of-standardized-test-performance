from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(s, i, candidate):
            if i == len(s):
                result.append(candidate)
                return

            if s[i].isalpha():
                backtrack(s, i + 1, candidate + s[i].lower())
                backtrack(s, i + 1, candidate + s[i].upper())
            else:
                backtrack(s, i + 1, candidate + s[i])

        backtrack(s, 0, '')
        return result
