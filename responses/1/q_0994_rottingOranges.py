from typing import List

class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh_count = 0
        rotten = []
        minutes = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        while fresh_count > 0 and rotten:
            next_rotten = []
            for i, j in rotten:
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh_count -= 1
                        next_rotten.append((x, y))
            rotten = next_rotten
            minutes += 1

        return minutes if fresh_count == 0 else -1
