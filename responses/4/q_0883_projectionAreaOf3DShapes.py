from typing import List

class Solution:
    
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area_xy = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
        area_xz = sum(max(row) for row in grid)
        area_yz = sum(max(col) for col in zip(*grid))
        
        return area_xy + area_xz + area_yz
