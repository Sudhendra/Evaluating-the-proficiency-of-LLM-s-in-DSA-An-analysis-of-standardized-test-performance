from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        dp = [0.0] * n
        for i in range(n):
            dp[i] = (prefix_sum[n] - prefix_sum[i]) / (n - i)

        for _ in range(k - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    dp[i] = max(dp[i], dp[j] + (prefix_sum[j] - prefix_sum[i]) / (j - i))

        return dp[0]
