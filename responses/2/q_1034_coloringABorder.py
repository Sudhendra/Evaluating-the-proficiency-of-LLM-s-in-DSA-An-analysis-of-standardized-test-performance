from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]:
        def is_boundary(r, c):
            if r == 0 or c == 0 or r == len(grid) - 1 or c == len(grid[0]) - 1:
                return True
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != grid[r][c]:
                    return True
            return False
        
        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == origin_color):
                return
            if is_boundary(r, c):
                border.add((r, c))
            seen.add((r, c))
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in seen and 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[r][c] == grid[nr][nc]:
                    dfs(nr, nc)
                    if (nr, nc) in border:
                        border.add((r, c))
        
        origin_color = grid[row][col]
        seen = set()
        border = set()
        dfs(row, col)
        for r, c in border:
            grid[r][c] = color
        return grid