from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        start_color = grid[row][col]

        def is_boundary(i, j):
            return i == 0 or i == m - 1 or j == 0 or j == n - 1

        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n

        def dfs(i, j):
            if not is_valid(i, j) or grid[i][j] != start_color:
                return False
            if is_boundary(i, j):
                return True

            grid[i][j] = -start_color
            border = all(dfs(x, y) for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)])
            if border:
                grid[i][j] = -start_color
            return border

        dfs(row, col)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == -start_color:
                    grid[i][j] = color
                elif grid[i][j] == start_color:
                    grid[i][j] = start_color

        return grid
