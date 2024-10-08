from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def find_island(grid, i, j, n, island):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = -1
            island.append((i, j))
            find_island(grid, i+1, j, n, island)
            find_island(grid, i-1, j, n, island)
            find_island(grid, i, j+1, n, island)
            find_island(grid, i, j-1, n, island)
        
        def expand(grid, island, n):
            steps = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while island:
                new_island = []
                for i, j in island:
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n:
                            if grid[x][y] == 1:
                                return steps
                            elif grid[x][y] == 0:
                                grid[x][y] = -1
                                new_island.append((x, y))
                steps += 1
                island = new_island
        
        n = len(grid)
        island1 = []
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    find_island(grid, i, j, n, island1)
                    break
            if island1:
                break

        return expand(grid, island1, n)
