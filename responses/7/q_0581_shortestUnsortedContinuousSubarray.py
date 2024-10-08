from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        min_val = float('inf')
        max_val = float('-inf')
        for i in range(left, right + 1):
            min_val = min(min_val, nums[i])
            max_val = max(max_val, nums[i])

        while left >= 0 and nums[left] > min_val:
            left -= 1

        while right < n and nums[right] < max_val:
            right += 1

        return right - left - 1
