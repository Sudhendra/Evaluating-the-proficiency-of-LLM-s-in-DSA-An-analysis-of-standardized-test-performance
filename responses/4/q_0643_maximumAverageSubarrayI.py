from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_k = sum(nums[:k])
        max_sum = sum_k
        for i in range(k, len(nums)):
            sum_k += nums[i] - nums[i - k]
            max_sum = max(max_sum, sum_k)
        return max_sum / k
