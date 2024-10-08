from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy_projection = sum(1 for row in grid for cell in row if cell > 0)
        xz_projection = sum(max(row) for row in grid)
        yz_projection = sum(max(row[i] for row in grid) for i in range(len(grid[0]))
        return xy_projection + xz_projection + yz_projection
