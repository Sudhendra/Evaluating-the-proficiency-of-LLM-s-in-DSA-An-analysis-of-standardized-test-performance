from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        original_color = grid[row][col]

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != original_color:
                return
            if (r, c) in borders:
                return
            
            borders.add((r, c))
            if r == 0 or r == m - 1 or c == 0 or c == n - 1 or any((nr, nc) not in borders for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]):
                border_cells.add((r, c))
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        borders = set()
        border_cells = set()
        dfs(row, col)

        for r, c in border_cells:
            grid[r][c] = color

        return grid
