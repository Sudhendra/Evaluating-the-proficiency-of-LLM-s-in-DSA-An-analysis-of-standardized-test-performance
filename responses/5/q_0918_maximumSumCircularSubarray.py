from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def max_subarray_sum(nums):
            max_so_far = max_ending_here = nums[0]
            for num in nums[1:]:
                max_ending_here = max(num, max_ending_here + num)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        
        total_sum = sum(nums)
        max_wraparound = total_sum + max_subarray_sum([-num for num in nums])
        return max(max_subarray_sum(nums), max_wraparound) if max(max_subarray_sum(nums), max_wraparound) != 0 else max(nums)
