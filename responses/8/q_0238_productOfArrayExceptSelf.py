from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        left_product, right_product = 1, 1
        
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]
            
            result[n - 1 - i] *= right_product
            right_product *= nums[n - 1 - i]
        
        return result
