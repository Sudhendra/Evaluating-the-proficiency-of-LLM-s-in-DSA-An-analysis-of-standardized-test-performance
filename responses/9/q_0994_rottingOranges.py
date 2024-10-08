from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0
        
        minutes = 0
        while queue:
            for _ in range(len(queue)):
                cur_x, cur_y = queue.popleft()
                for dx, dy in directions:
                    new_x, new_y = cur_x + dx, cur_y + dy
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        fresh_count -= 1
                        queue.append((new_x, new_y))
            minutes += 1

        return minutes - 1 if fresh_count == 0 else -1
