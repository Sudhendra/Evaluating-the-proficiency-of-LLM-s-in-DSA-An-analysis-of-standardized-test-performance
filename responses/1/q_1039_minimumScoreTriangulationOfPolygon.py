from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):
            for left in range(n):
                right = (left + gap) % n
                dp[left][right] = float('inf')
                for k in range(left + 1, right):
                    dp[left][right] = min(dp[left][right], dp[left][k] + dp[k][right] + values[left] * values[k] * values[right])

        return dp[0][n - 1]