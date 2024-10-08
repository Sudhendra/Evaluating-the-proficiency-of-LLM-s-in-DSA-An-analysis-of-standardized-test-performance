from typing import List

class Solution:
    """You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^{th}` day.

    Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

    * After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

    **Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
    """

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]  # dp[i][0] represents the maximum profit on day i without stock in hand, dp[i][1] represents the maximum profit on day i with stock in hand
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], (dp[i-2][0] if i >= 2 else 0) - prices[i])

        return dp[-1][0]
