from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, curr_sum, k, n, path, result):
            if k == 0 and curr_sum == n:
                result.append(path)
                return
            if k == 0 or curr_sum >= n:
                return
            for i in range(start, 10):
                backtrack(i + 1, curr_sum + i, k - 1, n, path + [i], result)
        
        result = []
        backtrack(1, 0, k, n, [], result)
        return result
