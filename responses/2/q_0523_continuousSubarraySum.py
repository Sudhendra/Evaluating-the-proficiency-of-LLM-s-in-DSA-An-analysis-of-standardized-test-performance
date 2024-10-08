from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum_mod_k = {0: -1}
        total_sum = 0
        
        for i, num in enumerate(nums):
            total_sum += num
            if k != 0:
                total_sum %= k
            
            if total_sum in prefix_sum_mod_k:
                if i - prefix_sum_mod_k[total_sum] > 1:
                    return True
            else:
                prefix_sum_mod_k[total_sum] = i
                
        return False
