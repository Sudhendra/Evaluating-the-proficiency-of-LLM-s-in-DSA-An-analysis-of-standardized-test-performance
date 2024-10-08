from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 2
                for x, y in directions:
                    dfs(i + x, j + y)

        def bfs():
            queue = deque()
            visited = set()

            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        queue.append((i, j))
                        visited.add((i, j))

            level = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    i, j = queue.popleft()
                    for x, y in directions:
                        ni, nj = i + x, j + y
                        if 0 <= ni < n and 0 <= nj < n:
                            if grid[ni][nj] == 0:
                                queue.append((ni, nj))
                                visited.add((ni, nj))
                            elif grid[ni][nj] == 1:
                                return level
                level += 1

        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        return bfs() - 1
