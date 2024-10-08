from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_sum = sum(nums[:k])
        left_sum = [0] * n
        left_max = 0

        # Calculate sums of all possible non-overlapping subarrays from left
        for i in range(k, n - 2 * k):
            window_sum += nums[i] - nums[i - k]
            if window_sum > left_max:
                left_sum[i] = i - k
                left_max = window_sum
            else:
                left_sum[i] = left_sum[i - 1]

        right_sum = [0] * n
        right_max = 0
        window_sum = sum(nums[-k:])

        # Calculate sums of all possible non-overlapping subarrays from right
        for i in range(n - 2 * k, k - 1, -1):
            window_sum += nums[i] - nums[i + k]
            if window_sum >= right_max:
                right_sum[i] = i
                right_max = window_sum
            else:
                right_sum[i] = right_sum[i + 1]

        max_sum = 0
        result = []

        # Find the maximum sum of three non-overlapping subarrays
        for i in range(k, n - k):
            left_idx = left_sum[i - 1]
            right_idx = right_sum[i + k]
            total = sum(nums[left_idx:left_idx + k]) + sum(nums[i:i + k]) + sum(nums[right_idx:right_idx + k])
            if total > max_sum:
                max_sum = total
                result = [left_idx, i, right_idx]

        return result
