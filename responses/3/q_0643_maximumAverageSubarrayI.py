from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        maximum = total

        for i in range(k, len(nums)):
            total += nums[i] - nums[i - k]
            maximum = max(maximum, total)

        return maximum / k
