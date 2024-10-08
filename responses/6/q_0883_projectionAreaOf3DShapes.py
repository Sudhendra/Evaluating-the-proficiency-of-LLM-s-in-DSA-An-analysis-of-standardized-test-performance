from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(v > 0 for row in grid for v in row)
        xz = sum(max(row) for row in grid)
        yz = sum(max(row[i] for row in grid) for i in range(len(grid)))
        
        return xy + xz + yz
