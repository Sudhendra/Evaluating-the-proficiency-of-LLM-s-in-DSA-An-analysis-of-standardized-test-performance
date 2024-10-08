from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_score = nums[-1] - nums[0]

        for i in range(len(nums) - 1):
            big = max(nums[i] + k, nums[-1] - k)
            small = min(nums[0] + k, nums[i + 1] - k)
            min_score = min(min_score, big - small)

        return min_score
