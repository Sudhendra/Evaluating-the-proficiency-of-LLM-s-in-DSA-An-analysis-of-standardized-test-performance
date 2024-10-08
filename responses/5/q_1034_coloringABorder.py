from typing import List

class Solution:
    def colorBorder(
        self, grid: List[List[int]], row: int, col: int, color: int
    ) -> List[List[int]:
        m, n = len(grid), len(grid[0])
        def is_border(r, c):
            if r == 0 or c == 0 or r == m - 1 or c == n - 1:
                return True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != color:
                    return True
            return False

        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] != color:
                return
            if is_border(r, c):
                grid[r][c] = -color
            else:
                grid[r][c] = -1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        dfs(row, col)
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    grid[i][j] = color
                else:
                    grid[i][j] = -grid[i][j]
        return grid
