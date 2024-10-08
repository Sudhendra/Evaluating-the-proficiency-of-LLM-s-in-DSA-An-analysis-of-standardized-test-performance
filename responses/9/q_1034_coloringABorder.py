from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]:
        m, n = len(grid), len(grid[0])
        original_color = grid[row][col]
        
        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] != original_color:
                return 1
            if visited[x][y]:
                return 0
            
            visited[x][y] = True
            is_border = 0 < x < m - 1 and 0 < y < n - 1 and all(grid[x + dx][y + dy] == original_color for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)))
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                is_border += dfs(x + dx, y + dy)
            
            if is_border < 4:
                grid[x][y] = color
            
            return is_border
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        dfs(row, col)
        return grid
