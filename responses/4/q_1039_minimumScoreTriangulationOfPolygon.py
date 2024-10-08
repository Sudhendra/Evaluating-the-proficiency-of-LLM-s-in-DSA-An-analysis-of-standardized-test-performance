from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):
            for i in range(n):
                j = (i + gap) % n
                dp[i][j] = float('inf')
                for k in range(i + 1, i + gap):
                    dp[i][j] = min(dp[i][j], dp[i][k % n] + dp[k % n][j] + values[i] * values[k % n] * values[j])

        return dp[0][n - 1]
