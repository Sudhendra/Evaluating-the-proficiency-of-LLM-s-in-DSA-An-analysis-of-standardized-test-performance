class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        
        for length in range(2, n+1):
            for start in range(1, n-length+2):
                min_cost = float('inf')
                for pivot in range(start, start+length-1):
                    cost = pivot + max(dp[start][pivot-1], dp[pivot+1][start+length-1])
                    min_cost = min(min_cost, cost)
                dp[start][start+length-1] = min_cost
        
        return dp[1][n]