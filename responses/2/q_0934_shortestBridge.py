from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def paint(grid, r, c, color):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != 1:
                return
            grid[r][c] = color
            paint(grid, r+1, c, color)
            paint(grid, r-1, c, color)
            paint(grid, r, c+1, color)
            paint(grid, r, c-1, color)
        
        def expand(grid, r, c, color):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return False
            if grid[r][c] == 0:
                grid[r][c] = color + 1
            return grid[r][c] == 1
        
        color = 2

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    paint(grid, r, c, color)
                    color += 1

        queue = deque([(r, c, 0) for r in range(len(grid) - 1) for c in range(len(grid[0] - 1)) if grid[r][c] == 2])

        while queue:
            r, c, dist = queue.popleft()
            if expand(grid, r-1, c, grid[r][c]) or expand(grid, r+1, c, grid[r][c]) or expand(grid, r, c-1, grid[r][c]) or expand(grid, r, c+1, grid[r][c]):
                return dist
            queue.extend([(r-1, c, dist+1), (r+1, c, dist+1), (r, c-1, dist+1), (r, c+1, dist+1)]
