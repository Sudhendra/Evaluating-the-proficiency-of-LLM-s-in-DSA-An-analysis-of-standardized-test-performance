from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j, index):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = index
            area = 1
            for dx, dy in direction:
                area += dfs(i + dx, j + dy, index)
            return area
        
        island_area = {0: 0}
        index = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_area[index] = dfs(i, j, index)
                    index += 1
        
        result = max(island_area.values())
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    connected_islands = set()
                    for dx, dy in direction:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] != 0:
                            connected_islands.add(grid[x][y])
                    result = max(result, sum(island_area[key] for key in connected_islands) + 1)
        
        return result
