from typing import List

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n) or grid[r][c] != 1:
                return 0
            grid[r][c] = 2
            size = 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                size += dfs(r+dr, c+dc)
            return size
        
        def is_stable(r, c):
            return r == 0 or any(grid[nr][nc] == 2 for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)])
        
        m, n = len(grid), len(grid[0])
        for i, j in hits:
            grid[i][j] -= 1
        
        for i in range(n):
            dfs(0, i)
        
        result = []
        for r, c in reversed(hits):
            grid[r][c] += 1
            if grid[r][c] == 1 and is_stable(r, c):
                result.append(dfs(r, c) - 1)
            else:
                result.append(0)
        
        return result[::-1]
