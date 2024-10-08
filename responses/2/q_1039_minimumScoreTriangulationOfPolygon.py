from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for d in range(2, n):
            for left in range(n):
                right = (left + d) % n
                for k in range(left+1, right):
                    dp[left][right] = min(dp[left][right] or float('inf'), dp[left][k] + dp[k][right] + values[left] * values[right] * values[k])

        return dp[0][n-1]
