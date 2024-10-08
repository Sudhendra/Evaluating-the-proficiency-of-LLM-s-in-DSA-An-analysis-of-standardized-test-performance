from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        def backtrack(path, nums, result):
            if not nums:
                result.append(path)
                return
            for i in range(len(nums)):
                backtrack(path + [nums[i]], nums[:i] + nums[i+1:], result)
        
        result = []
        backtrack([], nums, result)
        return result
