from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        new_grid = [['0'] * (n * 3) for _ in range(n * 3)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    new_grid[i * 3][j * 3 + 2] = new_grid[i * 3 + 1][j * 3 + 1] = new_grid[i * 3 + 2][j * 3] = '1'
                elif grid[i][j] == '\\':
                    new_grid[i * 3][j * 3] = new_grid[i * 3 + 1][j * 3 + 1] = new_grid[i * 3 + 2][j * 3 + 2] = '1'
        
        def dfs(x, y):
            if x < 0 or y < 0 or x >= n * 3 or y >= n * 3 or new_grid[x][y] == '1':
                return
            new_grid[x][y] = '1'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        count = 0
        for i in range(n * 3):
            for j in range(n * 3):
                if new_grid[i][j] == '0':
                    dfs(i, j)
                    count += 1
        
        return count
