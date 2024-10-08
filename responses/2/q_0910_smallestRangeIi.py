from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]  # Base case, without altering any elements

        for i in range(n - 1):
            a = max(nums[-1], nums[i] + 2 * k)
            b = min(nums[0] + 2 * k, nums[i + 1])
            ans = min(ans, a - b)

        return ans
