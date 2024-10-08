from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Calculate maximum subarray sum using Kadane's algorithm
        def kadane(nums):
            max_sum, cur_sum = nums[0], nums[0]
            for num in nums[1:]:
                cur_sum = max(num, cur_sum + num)
                max_sum = max(max_sum, cur_sum)
            return max_sum
        
        total_sum = sum(nums)
        max_kadane = kadane(nums)
        min_kadane = kadane([-num for num in nums])
        
        # Return maximum of two cases: max subarray sum using Kadane's algorithm and total sum minus min subarray sum
        return max(max_kadane, total_sum + min_kadane) if max_kadane > 0 else max_kadane
