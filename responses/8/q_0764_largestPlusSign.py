from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = {tuple(mine) for mine in mines}
        grid = [[0] * n for _ in range(n)]
        dp = [[0] * n for _ in range(n)]
        res = 0

        for mine in banned:
            grid[mine[0]][mine[1]] = 1

        for i in range(n):
            left = 0
            for j in range(n):
                if grid[i][j] == 1:
                    left = 0
                else:
                    left += 1
                dp[i][j] = left

            right = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    right = 0
                else:
                    right += 1
                dp[i][j] = min(dp[i][j], right)

        for j in range(n):
            up = 0
            for i in range(n):
                if grid[i][j] == 1:
                    up = 0
                else:
                    up += 1

                dp[i][j] = min(dp[i][j], up)

            down = 0
            for i in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    down = 0
                else:
                    down += 1

                dp[i][j] = min(dp[i][j], down)
                res = max(res, dp[i][j])

        return res
