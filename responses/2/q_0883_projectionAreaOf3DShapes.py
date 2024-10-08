from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy_projection = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
        xz_projection = sum(max(row) for row in grid)
        yz_projection = sum(max(col) for col in zip(*grid))
        return xy_projection + xz_projection + yz_projection