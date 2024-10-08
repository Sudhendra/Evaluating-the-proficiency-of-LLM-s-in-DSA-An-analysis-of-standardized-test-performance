from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        seen = {0: -1}
        current_sum = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            if k != 0:
                current_sum %= k
            if current_sum in seen:
                if i - seen[current_sum] > 1:
                    return True
            else:
                seen[current_sum] = i
        
        return False
