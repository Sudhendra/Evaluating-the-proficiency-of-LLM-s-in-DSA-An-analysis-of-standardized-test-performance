from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count_subarrays(arr: List[int], bound: int) -> int:
            count, cur_count = 0, 0
            for num in arr:
                cur_count = cur_count + 1 if num <= bound else 0
                count += cur_count
            return count
        
        return count_subarrays(nums, right) - count_subarrays(nums, left - 1)
