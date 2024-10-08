from typing import List

class Solution:
    
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        mod_count = {0: 1}
        
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += mod_count.get(prefix_sum, 0)
            mod_count[prefix_sum] = mod_count.get(prefix_sum, 0) + 1
        
        return count
