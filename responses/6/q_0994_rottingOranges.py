from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        rotten = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0

        while rotten:
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        fresh_count -= 1
                        rotten.append((new_x, new_y))

            minutes += 1

        return -1 if fresh_count > 0 else max(0, minutes - 1)
