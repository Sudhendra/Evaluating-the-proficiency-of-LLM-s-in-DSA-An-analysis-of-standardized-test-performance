from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(s, start, path, res):
            if start == len(s):
                res.append(''.join(path))
                return

            if s[start].isalpha():
                path.append(s[start].lower())
                backtrack(s, start + 1, path, res)
                path.pop()

                path.append(s[start].upper())
                backtrack(s, start + 1, path, res)
                path.pop()
            else:
                path.append(s[start])
                backtrack(s, start + 1, path, res)
                path.pop()

        res = []
        backtrack(s, 0, [], res)
        return res
