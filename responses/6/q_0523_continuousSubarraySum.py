from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < 2:
            return False
        
        seen = {0: -1}  # Initialize a dictionary with key 0 and value -1
        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            if k != 0:
                total_sum %= k
            if total_sum in seen:
                if i - seen[total_sum] > 1:
                    return True
            else:
                seen[total_sum] = i
        return False
