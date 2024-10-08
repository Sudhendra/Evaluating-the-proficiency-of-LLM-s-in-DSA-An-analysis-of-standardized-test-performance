from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        max_profit = 0
        left_profit = [0] * n
        right_profit = [0] * n
        
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_profit[i] = max(left_profit[i-1], prices[i] - min_price)
        
        max_price = prices[n-1]
        for i in range(n-2, -1, -1):
            max_price = max(max_price, prices[i])
            right_profit[i] = max(right_profit[i+1], max_price - prices[i])
        
        for i in range(n):
            max_profit = max(max_profit, left_profit[i] + right_profit[i])
        
        return max_profit
