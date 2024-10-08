from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]

        def helper(row1, col1, row2):
            col2 = row1 + col1 - row2
            if row1 >= n or col1 >= n or row2 >= n or col2 >= n or grid[row1][col1] == -1 or grid[row2][col2] == -1:
                return float('-inf')

            if dp[row1][col1][row2] != -1:
                return dp[row1][col1][row2]

            if row1 == n - 1 and col1 == n - 1:
                return grid[row1][col1]

            cherries = grid[row1][col1] + (col1 != col2) * grid[row2][col2]
            cherries += max(helper(row1+1, col1, row2+1), helper(row1, col1+1, row2+1), helper(row1+1, col1, row2), helper(row1, col1+1, row2))

            dp[row1][col1][row2] = cherries
            return cherries

        return max(0, helper(0, 0, 0))
