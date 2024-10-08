from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = low + (high - low) // 2
            count, left = 0, 0

            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left

            if count < k:
                low = mid + 1
            else:
                high = mid

        return low
