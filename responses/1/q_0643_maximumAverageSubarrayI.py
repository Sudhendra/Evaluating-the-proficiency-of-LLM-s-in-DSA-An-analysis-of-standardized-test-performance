from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        cur_sum = max_sum
        for i in range(k, len(nums)):
            cur_sum = cur_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, cur_sum)
        
        return max_sum / k
