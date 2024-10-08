class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        def calculate(i, j):
            if i >= j:
                return 0
            if dp[i][j]:
                return dp[i][j]
            
            min_cost = float("inf")
            for x in range((i + j) // 2, j):
                cost = x + max(calculate(i, x - 1), calculate(x + 1, j))
                min_cost = min(min_cost, cost)
            
            dp[i][j] = min_cost
            return dp[i][j]
        
        return calculate(1, n)
