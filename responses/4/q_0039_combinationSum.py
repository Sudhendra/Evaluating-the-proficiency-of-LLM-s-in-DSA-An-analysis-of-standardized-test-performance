from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if target - candidates[i] < 0:
                    break
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        res = []
        candidates.sort()
        backtrack(0, target, [])
        return res
