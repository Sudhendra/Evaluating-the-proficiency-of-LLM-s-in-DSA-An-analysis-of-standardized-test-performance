class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for start in range(n - 1, 0, -1):
            for end in range(start + 1, n + 1):
                dp[start][end] = min(x + max(dp[start][x - 1], dp[x + 1][end]) for x in range(start, end))
        return dp[1][n]
