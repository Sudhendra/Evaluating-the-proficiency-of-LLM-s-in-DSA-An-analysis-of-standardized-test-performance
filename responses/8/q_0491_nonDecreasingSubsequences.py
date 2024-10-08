from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path, res):
            if len(path) > 1:
                res.append(path[:])
            visited = set()
            for i in range(start, len(nums)):
                if (not path or nums[i] >= path[-1]) and nums[i] not in visited:
                    visited.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path, res)
                    path.pop()

        res = []
        backtrack(0, [], res)
        return res
