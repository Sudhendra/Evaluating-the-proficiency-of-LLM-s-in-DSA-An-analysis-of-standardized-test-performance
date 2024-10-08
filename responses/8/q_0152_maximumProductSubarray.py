from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        max_product = nums[0]
        min_product = nums[0]
        result = max_product
        
        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, max_product * num, min_product * num)
            min_product = min(num, max_product * num, min_product * num)
            max_product = temp_max
            result = max(max_product, result)
        
        return result
