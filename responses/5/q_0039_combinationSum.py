from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, res):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path, res)
                path.pop()
        
        candidates.sort()
        res = []
        backtrack(0, target, [], res)
        return res
