from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            max_sum = nums[0]
            current_sum = nums[0]
            for i in range(1, len(nums)):
                current_sum = max(nums[i], current_sum + nums[i])
                max_sum = max(max_sum, current_sum)
            return max_sum
        
        total_sum = sum(nums)
        max_sum_wrap = total_sum + kadane([-num for num in nums])
        max_sum_non_wrap = kadane(nums)
        
        return max(max_sum_wrap, max_sum_non_wrap) if max_sum_wrap != 0 else max_sum_non_wrap
