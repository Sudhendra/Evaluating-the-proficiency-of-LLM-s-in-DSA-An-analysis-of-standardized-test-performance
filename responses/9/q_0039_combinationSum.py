from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain, path, start):
            if remain < 0:
                return
            if remain == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                backtrack(remain - candidates[i], path + [candidates[i]], i)
        
        res = []
        candidates.sort()
        backtrack(target, [], 0)
        return res
