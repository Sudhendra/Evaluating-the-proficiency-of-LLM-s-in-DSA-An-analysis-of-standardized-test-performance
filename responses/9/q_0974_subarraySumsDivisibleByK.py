from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_count = {0: 1}  # The remainder of the sum of an empty array is 0
        
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += remainder_count.get(prefix_sum, 0)
            remainder_count[prefix_sum] = remainder_count.get(prefix_sum, 0) + 1
        
        return count
