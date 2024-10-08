class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    dfs(x, y)
        
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
        
        for j in range(cols):
            dfs(0, j)
            dfs(rows-1, j)
        
        return sum(sum(row) for row in grid)