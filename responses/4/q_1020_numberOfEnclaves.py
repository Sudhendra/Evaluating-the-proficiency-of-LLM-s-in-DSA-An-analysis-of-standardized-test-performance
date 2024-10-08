from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    dfs(grid, i + x, j + y)
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            dfs(grid, i, 0)
            dfs(grid, i, cols - 1)
        
        for j in range(cols):
            dfs(grid, 0, j)
            dfs(grid, rows - 1, j)
        
        return sum(grid[i][j] for i in range(rows) for j in range(cols))
