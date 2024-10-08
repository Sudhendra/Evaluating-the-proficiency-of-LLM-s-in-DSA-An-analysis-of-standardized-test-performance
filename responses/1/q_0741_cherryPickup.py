from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
        
        def dfs(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1 == c1 == r2 == n-1:
                return grid[n-1][n-1] if grid[n-1][n-1] != -1 else 0
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -float('inf')
            if dp[r1][c1][r2] != -1:
                return dp[r1][c1][r2]
            
            res = max(dfs(r1+1, c1, r2+1), dfs(r1, c1+1, r2), dfs(r1+1, c1, r2), dfs(r1, c1+1, r2+1))
            if res == -float('inf'):
                cell_cherries = 0
            else:
                cell_cherries = grid[r1][c1] + (r1 != r2) * grid[r2][c2]
                
            dp[r1][c1][r2] = cell_cherries + res
            
            return dp[r1][c1][r2]
        
        return max(0, dfs(0, 0, 0))
