from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        added = 0
        covered = 0
        i = 0
    
        while covered < n:
            if i < len(nums) and nums[i] <= covered + 1:
                covered += nums[i]
                i += 1
            else:
                covered += covered + 1
                added += 1
        
        return added
