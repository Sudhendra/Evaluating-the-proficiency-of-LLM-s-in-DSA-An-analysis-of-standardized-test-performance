from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_index = 0
        odd_index = 1
        n = len(nums)
        
        while even_index < n and odd_index < n:
            if nums[even_index] % 2 == 0:
                even_index += 2
            elif nums[odd_index] % 2 != 0:
                odd_index += 2
            else:
                nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
        
        return nums
