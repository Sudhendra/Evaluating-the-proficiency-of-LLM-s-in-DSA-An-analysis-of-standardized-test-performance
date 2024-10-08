from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        left_max_sum = [0] * n
        right_max_sum = [0] * n
        max_sum = 0

        for i in range(k, n - 2 * k + 1):
            curr_sum = prefix_sum[i] - prefix_sum[i - k]
            if curr_sum > max_sum:
                max_sum = curr_sum
                left_max_sum[i] = i - k
            else:
                left_max_sum[i] = left_max_sum[i - 1]

        max_sum = 0
        for i in range(n - k, 2 * k - 1, -1):
            curr_sum = prefix_sum[i + k] - prefix_sum[i]
            if curr_sum >= max_sum:
                max_sum = curr_sum
                right_max_sum[i] = i
            else:
                right_max_sum[i] = right_max_sum[i + 1]

        max_sum = 0
        result = [0, 0, 0]

        for i in range(k, n - 2 * k + 1):
            left_idx = left_max_sum[i - 1]
            right_idx = right_max_sum[i + k]

            curr_sum = (prefix_sum[i + k] - prefix_sum[i]) + (prefix_sum[left_idx + k] - prefix_sum[left_idx]) + (prefix_sum[right_idx + k] - prefix_sum[right_idx])

            if curr_sum > max_sum:
                max_sum = curr_sum
                result = [left_idx, i, right_idx]

        return result
