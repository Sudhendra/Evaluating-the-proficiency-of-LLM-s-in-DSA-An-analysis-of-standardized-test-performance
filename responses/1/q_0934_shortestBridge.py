from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
                return
            grid[x][y] = 2
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        def find_first_island():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        dfs(i, j)
                        return

        find_first_island()

        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0]):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))


        while queue:
            x, y, dist = queue.pop(0)
            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                if newX < 0 or newX >= len(grid) or newY < 0 or newY >= len(grid[0]):
                    continue
                if grid[newX][newY] == 1:
                    return dist
                if grid[newX][newY] == 0:
                    queue.append((newX, newY, dist + 1))
                grid[newX][newY] = 2