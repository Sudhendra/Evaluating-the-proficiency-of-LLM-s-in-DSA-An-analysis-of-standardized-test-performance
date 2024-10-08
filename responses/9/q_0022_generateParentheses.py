class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(res, cur, left, right):
            if len(cur) == n * 2:
                res.append(cur)
                return
            if left < n:
                backtrack(res, cur + '(', left + 1, right)
            if right < left:
                backtrack(res, cur + ')', left, right + 1)

        res = []
        backtrack(res, '', 0, 0)
        return res
