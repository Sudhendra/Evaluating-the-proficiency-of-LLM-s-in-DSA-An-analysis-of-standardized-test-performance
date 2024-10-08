from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    dfs(i+dx, j+dy)
        
        for i in range(len(grid)):
            dfs(i, 0)
            dfs(i, len(grid[0])-1)
        
        for j in range(len(grid[0])):
            dfs(0, j)
            dfs(len(grid)-1, j)
        
        return sum(sum(row) for row in grid)
