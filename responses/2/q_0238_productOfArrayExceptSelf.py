from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Calculate the product of all elements to the left of each element
        prod = 1
        for i in range(n):
            res[i] *= prod
            prod *= nums[i]
        
        # Calculate the product of all elements to the right of each element
        prod = 1
        for i in range(n-1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        
        return res
