from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = 2 * n - 1
        dp = [[float('-inf')] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for k in range(1, m):
            dp2 = [[float('-inf')] * n for _ in range(n)]
            for i in range(max(0, k - (n - 1)), min(n - 1, k) + 1):
                for j in range(max(0, k - (n - 1)), min(n - 1, k) + 1):
                    if grid[i][k - i] == -1 or grid[j][k - j] == -1:
                        continue
                    val = grid[i][k - i]
                    if i != j:
                        val += grid[j][k - j]
                    for pi in [i - 1, i]:
                        for pj in [j - 1, j]:
                            if pi >= 0 and pj >= 0:
                                dp2[i][j] = max(dp2[i][j], dp[pi][pj] + val)
            dp = dp2

        return max(0, dp[n - 1][n - 1])
