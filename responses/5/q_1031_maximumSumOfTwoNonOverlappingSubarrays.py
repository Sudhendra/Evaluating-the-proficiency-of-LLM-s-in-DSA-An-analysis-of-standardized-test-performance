from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        def max_subarray_sum(prefix_sum, length):
            max_sum = 0
            max_window_sum = 0
            for i in range(length, len(prefix_sum)):
                max_window_sum = max(max_window_sum, prefix_sum[i - length] - prefix_sum[i - length - length])
                max_sum = max(max_sum, max_window_sum + prefix_sum[i] - prefix_sum[i - length])
            return max_sum

        return max(max_subarray_sum(prefix_sum, firstLen), max_subarray_sum(prefix_sum, secondLen))