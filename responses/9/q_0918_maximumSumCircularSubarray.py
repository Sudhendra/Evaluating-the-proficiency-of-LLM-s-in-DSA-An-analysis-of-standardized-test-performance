from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            max_sum, cur_sum = float('-inf'), 0
            for num in nums:
                cur_sum = num + max(cur_sum, 0)
                max_sum = max(max_sum, cur_sum)
            return max_sum
        
        total_sum = sum(nums)
        max_sum_wrap = total_sum + kadane([-num for num in nums])
        return max(kadane(nums), max_sum_wrap) if max(nums) > 0 else max(nums)
