from typing import List
from collections import Counter

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, max(nums) - min(nums)
        while low < high:
            mid = (low + high) // 2
            count, left = 0, 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low
