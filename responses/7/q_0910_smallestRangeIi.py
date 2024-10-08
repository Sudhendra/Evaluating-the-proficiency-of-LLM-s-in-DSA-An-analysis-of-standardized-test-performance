from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]

        for i in range(n - 1):
            min_val = min(nums[0] + k, nums[i + 1] - k)
            max_val = max(nums[i] + k, nums[-1] - k)
            ans = min(ans, max_val - min_val)

        return ans
