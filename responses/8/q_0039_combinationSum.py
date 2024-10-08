class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path, res)
                path.pop()

        res = []
        candidates.sort()
        backtrack(0, target, [], res)
        return res
