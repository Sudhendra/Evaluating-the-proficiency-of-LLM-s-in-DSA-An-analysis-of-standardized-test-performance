class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[j] * values[k])

        return dp[0][n - 1]
