from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        desired_sum = total_sum // 2
        dp = [False] * (desired_sum + 1)
        dp[0] = True

        for num in nums:
            for j in range(desired_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[desired_sum]
