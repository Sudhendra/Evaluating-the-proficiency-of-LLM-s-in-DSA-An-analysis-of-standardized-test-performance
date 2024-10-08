from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_pos = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
                non_zero_pos += 1
