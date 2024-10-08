from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = current_max = max_sum = current_min = min_sum = nums[0]
        
        for num in nums[1:]:
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)
            
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)
            
            total_sum += num
        
        if total_sum == min_sum:  # case where all elements are negative
            return max_sum
        return max(max_sum, total_sum - min_sum)
