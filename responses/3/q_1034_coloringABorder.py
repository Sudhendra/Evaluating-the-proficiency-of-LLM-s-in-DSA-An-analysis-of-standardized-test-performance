class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]:
        def is_border(r, c):
            if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                return True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and seen[nr][nc] and grid[nr][nc] != grid[r][c]:
                    return True
            return False

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or seen[r][c] or grid[r][c] != grid[row][col]:
                return
            seen[r][c] = True
            if is_border(r, c):
                grid[r][c] = color
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc)

        m, n = len(grid), len(grid[0])
        seen = [[False for _ in range(n)] for _ in range(m)]
        dfs(row, col)
        return grid
