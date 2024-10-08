from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, left, right, n, res):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right, n, res)
            if right < left:
                backtrack(s + ')', left, right + 1, n, res)

        res = []
        backtrack('', 0, 0, n, res)
        return res
