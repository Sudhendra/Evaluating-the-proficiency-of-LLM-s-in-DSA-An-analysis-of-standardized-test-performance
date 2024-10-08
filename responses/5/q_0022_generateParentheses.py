from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(res, current_str, open_count, close_count, max_pairs):
            if len(current_str) == max_pairs * 2:
                res.append(current_str)
                return
            if open_count < max_pairs:
                backtrack(res, current_str + "(", open_count + 1, close_count, max_pairs)
            if close_count < open_count:
                backtrack(res, current_str + ")", open_count, close_count + 1, max_pairs)

        res = []
        backtrack(res, "", 0, 0, n)
        return res
