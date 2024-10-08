from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path, res):
            if len(path) > 1:
                res.append(path[:])
            if len(path) == len(nums):
                return
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path, res)
                    path.pop()
        
        res = []
        backtrack(0, [], res)
        return res
