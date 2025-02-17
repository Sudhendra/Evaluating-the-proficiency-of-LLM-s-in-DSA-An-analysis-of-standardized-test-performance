from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n+1)

        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        dp = [[0.0] * (k+1) for _ in range(n)]

        for i in range(n):
            dp[i][1] = (prefix_sum[n] - prefix_sum[i]) / (n - i)

        for i in range(n-1, -1, -1):
            for j in range(2, k+1):
                for p in range(i+1, n):
                    dp[i][j] = max(dp[i][j], (prefix_sum[p] - prefix_sum[i]) / (p - i) + dp[p][j-1])

        return dp[0][k]
