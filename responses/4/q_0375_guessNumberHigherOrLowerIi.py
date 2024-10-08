class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for diff in range(1, n):
            for start in range(1, n - diff + 1):
                end = start + diff
                dp[start][end] = min(x + max(dp[start][x - 1], dp[x + 1][end]) for x in range(start, end))
        return dp[1][n]
