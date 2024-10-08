from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, index):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = index
                return 1 + sum(dfs(i+d[0], j+d[1], index) for d in [(0, 1), (0, -1), (1, 0), (-1, 0)])
            return 0
        
        area_map = {}
        index = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area_map[index] = dfs(i, j, index)
                    index += 1
        
        max_area = max(area_map.values(), default=0)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    connected_area = set(grid[ni][nj] for ni, nj in [(i+d[0], j+d[1]) for d in [(0, 1), (0, -1), (1, 0), (-1, 0)] if 0 <= i+d[0] < len(grid) and 0 <= j+d[1] < len(grid[0)]])
                    max_area = max(max_area, 1 + sum(area_map[index] for index in connected_area))
        
        return max_area
