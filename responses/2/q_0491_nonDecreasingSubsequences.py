from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) >= 2:
                result.append(path[:])
            if start == len(nums):
                return
            visited = set()
            for i in range(start, len(nums)):
                if nums[i] in visited:
                    continue
                if not path or nums[i] >= path[-1]:
                    visited.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
        
        result = []
        backtrack(0, [])
        return result
