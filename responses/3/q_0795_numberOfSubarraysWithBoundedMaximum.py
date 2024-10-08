from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def countSubarrays(nums: List[int], bound: int) -> int:
            count, cur = 0, 0
            for num in nums:
                cur = cur + 1 if num <= bound else 0
                count += cur
            return count
        
        return countSubarrays(nums, right) - countSubarrays(nums, left - 1)
