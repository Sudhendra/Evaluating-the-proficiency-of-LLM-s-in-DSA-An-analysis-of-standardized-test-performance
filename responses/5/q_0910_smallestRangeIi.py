from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        min_score = nums[-1] - nums[0]

        for i in range(n - 1):
            max_num = max(nums[i] + k, nums[-1] - k)
            min_num = min(nums[0] + k, nums[i + 1] - k)
            min_score = min(min_score, max_num - min_num)

        return min_score
