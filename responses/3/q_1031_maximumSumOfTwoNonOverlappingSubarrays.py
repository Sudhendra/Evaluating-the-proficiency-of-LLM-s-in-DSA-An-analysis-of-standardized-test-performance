from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        result = 0
        max_sum_first = self.max_sum_subarray(prefix_sum, firstLen)
        max_sum_second = self.max_sum_subarray(prefix_sum, secondLen)

        for i in range(len(nums)):
            sum_first = prefix_sum[i + firstLen] - prefix_sum[i]
            for j in range(len(nums)):
                if j + secondLen <= i or j >= i + firstLen:
                    sum_second = prefix_sum[j + secondLen] - prefix_sum[j]
                    result = max(result, sum_first + sum_second)

        return result

    def max_sum_subarray(self, prefix_sum, size):
        max_sum = 0
        for i in range(size, len(prefix_sum)):
            max_sum = max(max_sum, prefix_sum[i] - prefix_sum[i - size])
        return max_sum