from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_idx = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_idx], nums[i] = nums[i], nums[non_zero_idx]
                non_zero_idx += 1
