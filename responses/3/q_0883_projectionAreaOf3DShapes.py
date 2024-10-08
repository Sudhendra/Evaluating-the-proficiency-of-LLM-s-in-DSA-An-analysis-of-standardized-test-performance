class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy_projection_area = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
        xz_projection_area = sum(max(row) for row in grid)
        yz_projection_area = sum(max(row[j] for row in grid) for j in range(n))
        return xy_projection_area + xz_projection_area + yz_projection_area