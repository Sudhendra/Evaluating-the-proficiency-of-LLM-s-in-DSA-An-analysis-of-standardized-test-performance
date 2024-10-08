class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s="", open_count=0, close_count=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)

        result = []
        backtrack()
        return result
