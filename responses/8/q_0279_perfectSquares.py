class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * n
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        
        for square in squares:
            for i in range(square, n + 1):
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]
