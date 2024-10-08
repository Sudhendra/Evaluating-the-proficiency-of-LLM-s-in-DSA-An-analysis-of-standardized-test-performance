from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        max_k = 2
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]

        for k in range(max_k + 1):
            dp[0][k][1] = -prices[0]

        for i in range(1, n):
            for k in range(1, max_k + 1):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        return dp[n-1][max_k][0]
