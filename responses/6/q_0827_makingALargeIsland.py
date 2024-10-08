from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j, index):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j] = index
            return 1 + dfs(grid, i+1, j, index) + dfs(grid, i-1, j, index) + dfs(grid, i, j+1, index) + dfs(grid, i, j-1, index)

        def get_neighbors_indices(grid, i, j):
            neighbors = set()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    neighbors.add(grid[x][y])
            return neighbors

        def largest_connected_area(grid):
            index = 2
            areas = {0: 0}
            max_area = 0

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        area = dfs(grid, i, j, index)
                        areas[index] = area
                        max_area = max(max_area, area)
                        index += 1

            return max_area, areas

        max_area, areas = largest_connected_area(grid)
        
        for i in range(len(grid)):
            for j in range(len(grid[0]):
                if grid[i][j] == 0:
                    neighbors = get_neighbors_indices(grid, i, j)
                    total_area = 1
                    for neighbor in neighbors:
                        total_area += areas[neighbor]
                    max_area = max(max_area, total_area)
        
        return max_area
