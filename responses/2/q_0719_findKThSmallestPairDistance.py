from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            count, left = 0, 0
            for right, num in enumerate(nums):
                while num - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k
        
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid
            else:
                low = mid + 1
        return low