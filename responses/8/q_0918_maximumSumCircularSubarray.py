from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            max_sum = curr_sum = nums[0]
            for num in nums[1:]:
                curr_sum = max(num, curr_sum + num)
                max_sum = max(max_sum, curr_sum)
            return max_sum

        total_sum = sum(nums)
        max_wrap = total_sum - minSubArraySum(nums)
        max_no_wrap = kadane(nums)
        
        return max(max_no_wrap, max_wrap) if max_wrap != 0 else max_no_wrap

def minSubArraySum(nums):
    min_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = min(num, curr_sum + num)
        min_sum = min(min_sum, curr_sum)
    return min_sum
