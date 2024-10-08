from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Initialize a 2D DP table to store the minimum path sum up to each cell
        dp = [[0] * n for _ in range(m)]
        
        # Fill the first cell with the value of the original grid
        dp[0][0] = grid[0][0]
        
        # Fill the first row with accumulated sums
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
            
        # Fill the first column with accumulated sums
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        # Fill the rest of the table by choosing the minimum path sum from the top or left
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
