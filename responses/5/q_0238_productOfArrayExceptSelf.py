from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Calculate the product of all elements to the left of each element
        left_product = 1
        for i in range(n):
            output[i] *= left_product
            left_product *= nums[i]
        
        # Calculate the product of all elements to the right of each element
        right_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output