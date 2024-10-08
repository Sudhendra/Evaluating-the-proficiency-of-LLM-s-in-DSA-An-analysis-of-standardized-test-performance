from collections import deque

class Solution:
    def shortestBridge(self, grid):
        def find_first_island():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return i, j

        def paint_island(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 2
                paint_island(i - 1, j)
                paint_island(i + 1, j)
                paint_island(i, j - 1)
                paint_island(i, j + 1)

        def expand_island():
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                i, j, depth = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        if grid[ni][nj] == 1:
                            return depth
                        elif grid[ni][nj] == 0:
                            queue.append((ni, nj, depth + 1))
                            grid[ni][nj] = 2

        row, col = find_first_island()
        paint_island(row, col)

        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        return expand_island()        

# Implement additional solutions below if needed
