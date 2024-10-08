from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]

        for i in range(n - 1):
            high = max(nums[-1], nums[i] + 2 * k)
            low = min(nums[0] + 2 * k, nums[i + 1])
            ans = min(ans, high - low)

        return ans
