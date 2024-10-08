from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            current_sum = max_sum = nums[0]
            for num in nums[1:]:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            return max_sum
        
        total_sum = sum(nums)
        max_kadane = kadane(nums)
        max_wrap = total_sum + kadane([-num for num in nums])
        
        return max(max_kadane, max_wrap) if max_kadane > 0 else max_kadane
