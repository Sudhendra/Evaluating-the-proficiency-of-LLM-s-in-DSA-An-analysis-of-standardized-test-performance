from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    dfs(i + di, j + dj)

        # Mark connected land cells that are reachable as safe
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1) and grid[i][j] == 1:
                    dfs(i, j)

        # Count remaining land cells that are not safe (enclosed)
        return sum(sum(row) for row in grid)

# Test cases
s = Solution()
print(s.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])) # Output: 3
print(s.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])) # Output: 0
