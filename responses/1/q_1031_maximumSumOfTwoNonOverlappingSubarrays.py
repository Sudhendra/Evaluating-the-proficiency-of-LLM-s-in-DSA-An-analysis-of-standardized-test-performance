from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        def max_sum_subarray(length):
            max_sum = 0
            for i in range(length, n + 1):
                max_sum = max(max_sum, prefix_sum[i] - prefix_sum[i - length])
            return max_sum

        result = 0
        for i in range(1, n):
            left_sum = max_sum_subarray(i)
            right_sum = max_sum_subarray(n - i)
            result = max(result, left_sum + max_sum_subarray(secondLen), right_sum + max_sum_subarray(firstLen))

        return result
