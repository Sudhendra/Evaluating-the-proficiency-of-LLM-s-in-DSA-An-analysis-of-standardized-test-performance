from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1, n):
            if i == 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i], dp[i-2][0] - prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
        
        return dp[n-1][0]

# Example usage
solution = Solution()
prices1 = [1, 2, 3, 0, 2]
prices2 = [1]
print(solution.maxProfit(prices1))  # Output: 3
print(solution.maxProfit(prices2))  # Output: 0
