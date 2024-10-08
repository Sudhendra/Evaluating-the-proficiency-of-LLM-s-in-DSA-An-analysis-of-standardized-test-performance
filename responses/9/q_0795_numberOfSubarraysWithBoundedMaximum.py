from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def countSubarraysWithMaxInRange(arr: List[int], bound: int) -> int:
            count = 0
            cur_count = 0
            for num in arr:
                cur_count = cur_count + 1 if num <= bound else 0
                count += cur_count
            return count
        
        return countSubarraysWithMaxInRange(nums, right) - countSubarraysWithMaxInRange(nums, left - 1)
