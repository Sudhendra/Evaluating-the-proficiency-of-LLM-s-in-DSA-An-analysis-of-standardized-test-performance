from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0

        if k > n // 2:  # If k is large, we can perform as many transactions as we want
            max_profit = 0
            for i in range(1, n):
                max_profit += max(prices[i] - prices[i - 1], 0)
            return max_profit

        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            max_so_far = float('-inf')
            for j in range(1, n):
                max_so_far = max(max_so_far, dp[i - 1][j - 1] - prices[j - 1])
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_so_far)

        return dp[k][-1]
