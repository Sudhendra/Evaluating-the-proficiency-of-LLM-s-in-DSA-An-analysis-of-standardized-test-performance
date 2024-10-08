from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n < 3 * k:
            return []

        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)

        left_max_sum = [0] * n
        left_max_index = [0] * n
        right_max_sum = [0] * n
        right_max_index = [0] * n

        total_sum = prefix_sums[k] - prefix_sums[0]
        for i in range(k, n):
            cur_sum = prefix_sums[i + 1] - prefix_sums[i - k + 1]
            if cur_sum > total_sum:
                total_sum = cur_sum
                left_max_sum[i] = total_sum
                left_max_index[i] = i - k + 1
            else:
                left_max_sum[i] = total_sum
                left_max_index[i] = left_max_index[i - 1]

        total_sum = prefix_sums[n] - prefix_sums[n - k]
        for i in range(n - k - 1, -1, -1):
            cur_sum = prefix_sums[i + k] - prefix_sums[i]
            if cur_sum >= total_sum:
                total_sum = cur_sum
                right_max_sum[i] = total_sum
                right_max_index[i] = i
            else:
                right_max_sum[i] = total_sum
                right_max_index[i] = right_max_index[i + 1]

        max_sum = 0
        res = []
        for i in range(k, n - 2 * k + 1):
            cur_sum = left_max_sum[i - 1] + right_max_sum[i + k]
            if cur_sum > max_sum:
                max_sum = cur_sum
                res = [left_max_index[i - 1], i, right_max_index[i + k]]

        return res
