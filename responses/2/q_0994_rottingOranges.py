class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        if fresh_count == 0:
            return 0

        minutes = 0

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        fresh_count -= 1
                        grid[nx][ny] = 2
                        queue.append((nx, ny))

            minutes += 1

        return max(0, minutes - 1) if fresh_count == 0 else -1