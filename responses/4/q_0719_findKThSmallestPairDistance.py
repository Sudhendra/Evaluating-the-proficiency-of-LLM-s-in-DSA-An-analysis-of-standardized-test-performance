from typing import List

class Solution:
    def countPairs(self, nums: List[int], mid: int) -> int:
        count = 0
        left, right = 0, 0
        n = len(nums)
        
        while right < n:
            while nums[right] - nums[left] > mid:
                left += 1
            count += right - left
            right += 1
        
        return count

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left = 0
        right = nums[-1] - nums[0]
        
        while left < right:
            mid = left + (right - left) // 2
            count = self.countPairs(nums, mid)
            
            if count >= k:
                right = mid
            else:
                left = mid + 1
        
        return left
