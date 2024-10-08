from typing import List

class Solution:
    
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            if len(path) > 1:
                res.append(path[:])
            
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
        
        res = []
        backtrack(0, [])
        return res