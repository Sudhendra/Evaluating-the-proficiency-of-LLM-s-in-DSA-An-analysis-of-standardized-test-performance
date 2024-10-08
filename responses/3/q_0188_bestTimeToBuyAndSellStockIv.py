from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        
        n = len(prices)
        if k >= n // 2:  # Unlimited transactions
            max_profit = 0
            for i in range(1, n):
                max_profit += max(prices[i] - prices[i - 1], 0)
            return max_profit
        
        dp = [[0] * n for _ in range(k+1)]
        for i in range(1, k+1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i-1][j] - prices[j])
        
        return dp[k][n-1]