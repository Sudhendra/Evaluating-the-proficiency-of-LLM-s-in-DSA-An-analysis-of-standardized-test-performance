from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal area
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                area += 1
                grid[i][j] = 0
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    dfs(ni, nj)

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0]):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    max_area = max(max_area, area)
        
        return max_area
