from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for idx in range(n - 1, 1, -1):
            left, right = 0, idx - 1
            while left < right:
                if nums[left] + nums[right] > nums[idx]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
        
        return count
