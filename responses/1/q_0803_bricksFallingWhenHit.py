from typing import List

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] != 1:
                return 0
            grid[r][c] = 2
            size = 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                size += dfs(r+dr, c+dc)
            return size

        def is_connected(r, c):
            return r == 0 or any((0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 2) for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)])

        m, n = len(grid), len(grid[0])

        for r, c in hits:
            grid[r][c] -= 1

        for c in range(n):
            dfs(0, c)

        result = []
        for r, c in reversed(hits):
            grid[r][c] += 1
            if grid[r][c] == 1 and is_connected(r, c):
                result.append(dfs(r, c) - 1)
            else:
                result.append(0)
        return result[::-1]
