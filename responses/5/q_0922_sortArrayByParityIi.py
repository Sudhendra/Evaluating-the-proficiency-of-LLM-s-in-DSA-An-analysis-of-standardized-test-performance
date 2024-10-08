from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_idx, odd_idx = 0, 1
        n = len(nums)

        while even_idx < n and odd_idx < n:
            if nums[even_idx] % 2 == 0:
                even_idx += 2
            else:
                while nums[odd_idx] % 2 == 1:
                    odd_idx += 2
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]

        return nums
