from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        dp = [[0.0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[i][1] = prefix_sum[i] / i

        for kk in range(2, k + 1):  # partitions
            for i in range(kk, n + 1):  # elements
                for j in range(kk - 1, i):  # last partition end
                    dp[i][kk] = max(dp[i][kk], dp[j][kk - 1] + (prefix_sum[i] - prefix_sum[j]) / (i - j))

        return dp[n][k]
