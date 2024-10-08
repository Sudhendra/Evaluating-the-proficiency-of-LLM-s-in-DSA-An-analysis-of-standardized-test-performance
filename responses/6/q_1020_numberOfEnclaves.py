from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == 0:
                return
            grid[row][col] = 0
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        for i in range(len(grid)):
            dfs(i, 0)
            dfs(i, len(grid[0]) - 1)
        
        for j in range(len(grid[0])):
            dfs(0, j)
            dfs(len(grid) - 1, j)
        
        return sum(row.count(1) for row in grid)
