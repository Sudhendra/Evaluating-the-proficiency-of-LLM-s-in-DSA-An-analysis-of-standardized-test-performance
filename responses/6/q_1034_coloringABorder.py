from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        original_color = grid[row][col]
        visited = set()

        def is_border(r, c):
            return r == 0 or c == 0 or r == m - 1 or c == n - 1

        def dfs(r, c):
            if (r, c) in visited:
                return
            visited.add((r, c))
            is_curr_border = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] != original_color:
                        is_curr_border = True
                    elif (nr, nc) not in visited:
                        dfs(nr, nc)
            if is_curr_border or is_border(r, c):
                grid[r][c] = color

        dfs(row, col)
        return grid
