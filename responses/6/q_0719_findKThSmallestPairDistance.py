from typing import List
from collections import Counter

class Solution:
    def countPairs(self, nums: List[int], mid: int) -> int:
        count = 0
        left = 0
        for right, num in enumerate(nums):
            while num - nums[left] > mid:
                left += 1
            count += right - left
        return count
    
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0
        high = max(nums) - min(nums)
        
        while low < high:
            mid = (low + high) // 2
            count = self.countPairs(nums, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid
                
        return low
