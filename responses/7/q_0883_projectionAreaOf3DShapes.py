from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy = yz = zx = 0

        for i in range(n):
            max_row = max_col = 0
            for j in range(n):
                if grid[i][j] > 0:
                    xy += 1
                max_row = max(max_row, grid[i][j])
                max_col = max(max_col, grid[j][i])
            yz += max_row
            zx += max_col

        return xy + yz + zx
