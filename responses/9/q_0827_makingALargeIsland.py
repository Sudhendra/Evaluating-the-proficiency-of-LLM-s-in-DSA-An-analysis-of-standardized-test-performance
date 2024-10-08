from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, index):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = index
                return 1 + sum(dfs(x, y, index) for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)))
            return 0

        areas = {0: 0}
        index = 2
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    areas[index] = dfs(i, j, index)
                    max_area = max(max_area, areas[index])
                    index += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    seen = set()
                    for x, y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 0:
                            seen.add(grid[x][y])
                    max_area = max(max_area, 1 + sum(areas[index] for index in seen))

        return max_area
