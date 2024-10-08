from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        if k >= n // 2:  # If k is large enough to cover all possible transactions
            max_profit = 0
            for i in range(1, n):
                max_profit += max(0, prices[i] - prices[i-1])
            return max_profit

        dp = [[0] * n for _ in range(k + 1)]

        for j in range(1, k + 1):
            max_diff = -prices[0]
            for i in range(1, n):
                dp[j][i] = max(dp[j][i-1], prices[i] + max_diff)
                max_diff = max(max_diff, dp[j-1][i] - prices[i])

        return dp[k][n-1]
