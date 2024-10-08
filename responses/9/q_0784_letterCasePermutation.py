from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(i, path):
            if i == len(s):
                res.append(''.join(path))
                return
            if s[i].isalpha():
                backtrack(i+1, path + [s[i].lower()])
                backtrack(i+1, path + [s[i].upper()])
            else:
                backtrack(i+1, path + [s[i]])

        res = []
        backtrack(0, [])
        return res
