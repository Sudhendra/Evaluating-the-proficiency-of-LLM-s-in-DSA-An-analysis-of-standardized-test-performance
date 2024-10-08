from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp1 = [0] * n
        dp2 = [0] * n

        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp1[i] = max(dp1[i - 1], prices[i] - min_price)

        max_price = prices[n - 1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            dp2[i] = max(dp2[i + 1], max_price - prices[i])

        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, dp1[i] + dp2[i])

        return max_profit
