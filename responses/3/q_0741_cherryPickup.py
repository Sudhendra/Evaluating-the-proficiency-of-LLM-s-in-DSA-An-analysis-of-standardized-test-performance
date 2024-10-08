from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
        
        def dfs(row1, col1, col2):
            row2 = row1 + col1 - col2
            if row1 == n or col1 == n or col2 == n or row2 == n:
                return 0
            
            if grid[row1][col1] == -1 or grid[row2][col2] == -1:
                return 0
            
            if dp[row1][col1][col2] != -1:
                return dp[row1][col1][col2]
            
            result = max(
                dfs(row1+1, col1, col2), 
                dfs(row1, col1+1, col2), 
                dfs(row1+1, col1, col2+1),
                dfs(row1, col1+1, col2+1)
            )
            
            if row1 == row2 and col1 == col2:
                result += grid[row1][col1]
            else:
                result += grid[row1][col1] + grid[row2][col2]
            
            dp[row1][col1][col2] = result
            return result
        
        return max(0, dfs(0, 0, 0))
