from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(s, idx, path, res):
            if idx == len(s):
                res.append(''.join(path))
                return
            if s[idx].isalpha():
                path.append(s[idx].lower())
                backtrack(s, idx + 1, path, res)
                path.pop()
                path.append(s[idx].upper())
                backtrack(s, idx + 1, path, res)
                path.pop()
            else:
                path.append(s[idx])
                backtrack(s, idx + 1, path, res)
                path.pop()
        
        res = []
        backtrack(s, 0, [], res)
        return res
