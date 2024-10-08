from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_count = 0
        rotten_oranges = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0

        while rotten_oranges and fresh_count:
            minutes += 1
            for _ in range(len(rotten_oranges)):
                x, y = rotten_oranges.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        rotten_oranges.append((nx, ny))
                        fresh_count -= 1

        return minutes if fresh_count == 0 else -1
