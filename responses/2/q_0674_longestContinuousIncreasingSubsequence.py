from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_length = 1
        curr_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_length += 1
                max_length = max(max_length, curr_length)
            else:
                curr_length = 1
        
        return max_length
