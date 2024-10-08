from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_subarrays(max_val):
            count = 0
            res = 0
            for num in nums:
                if num <= max_val:
                    count += 1
                    res += count
                else:
                    count = 0
            return res
        
        return count_subarrays(right) - count_subarrays(left - 1)
