class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(ans, s, left, right, n):
            if len(s) == 2 * n:
                ans.append("".join(s))
                return
            if left < n:
                s.append("(")
                backtrack(ans, s, left + 1, right, n)
                s.pop()
            if right < left:
                s.append(")")
                backtrack(ans, s, left, right + 1, n)
                s.pop()

        ans = []
        backtrack(ans, [], 0, 0, n)
        return ans
