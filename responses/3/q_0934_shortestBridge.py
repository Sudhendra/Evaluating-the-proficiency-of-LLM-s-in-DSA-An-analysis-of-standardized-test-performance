from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j, visited, island):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or (i, j) in visited:
                return
            visited.add((i, j))
            island.append((i, j))
            dfs(grid, i + 1, j, visited, island)
            dfs(grid, i - 1, j, visited, island)
            dfs(grid, i, j + 1, visited, island)
            dfs(grid, i, j - 1, visited, island)

        def bfs(grid, island, visited):
            queue = island.copy()
            level = 0
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.pop(0)
                    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or (i, j) in visited:
                        continue
                    if grid[i][j] == 1:
                        return level - 1
                    visited.add((i, j))
                    queue.append((i + 1, j))
                    queue.append((i - 1, j))
                    queue.append((i, j + 1))
                    queue.append((i, j - 1))
                level += 1

        islands = []
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    island = []
                    dfs(grid, i, j, visited, island)
                    islands.append(island)

        return bfs(grid, islands[0], set(islands[0]))