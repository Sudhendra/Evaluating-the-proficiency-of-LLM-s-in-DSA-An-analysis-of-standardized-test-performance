from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        current_sum = max_sum
        
        for i in range(1, len(nums) - k + 1):
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            max_sum = max(max_sum, current_sum)
        
        return max_sum / k
