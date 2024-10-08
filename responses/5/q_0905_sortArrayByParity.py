from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_idx = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[even_idx] = nums[even_idx], nums[i]
                even_idx += 1
        return nums
