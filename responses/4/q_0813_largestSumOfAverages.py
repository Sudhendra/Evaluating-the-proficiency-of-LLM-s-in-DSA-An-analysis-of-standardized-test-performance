from functools import lru_cache
from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        @lru_cache(None)
        def average(i, j):
            return (prefix_sum[j] - prefix_sum[i]) / (j - i) if j > i else 0

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = average(0, i)

        for kk in range(2, k+1):
            for i in range(kk, n+1):
                for j in range(kk - 1, i):
                    dp[i][kk] = max(dp[i][kk], dp[j][kk-1] + average(j, i))

        return dp[n][k]
