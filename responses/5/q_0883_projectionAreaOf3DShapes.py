from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy_projection = sum(v > 0 for row in grid for v in row)
        yz_projection = sum(max(row) for row in grid)
        xz_projection = sum(max(row[i] for row in grid) for i in range(n))
        return xy_projection + yz_projection + xz_projection
