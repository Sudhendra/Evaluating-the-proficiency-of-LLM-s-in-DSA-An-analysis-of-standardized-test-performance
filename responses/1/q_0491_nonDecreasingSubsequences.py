from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path, res):
            if len(path) >= 2:
                res.append(path[:])
            
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used or (path and nums[i] < path[-1]):
                    continue
                
                used.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1, path, res)
                path.pop()
        
        res = []
        backtrack(0, [], res)
        return res