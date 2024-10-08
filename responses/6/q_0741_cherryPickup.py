from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def cherryHelper(grid, r1, c1, r2, dp):
            c2 = r1 + c1 - r2
            
            if r1 == len(grid) or c1 == len(grid) or r2 == len(grid) or c2 == len(grid) or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            if dp[r1][c1][r2] is not None:
                return dp[r1][c1][r2]
            
            if r1 == len(grid) - 1 and c1 == len(grid) - 1:
                return grid[r1][c1]
            
            result = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
            result += max(cherryHelper(grid, r1 + 1, c1, r2 + 1, dp), cherryHelper(grid, r1, c1 + 1, r2 + 1, dp), cherryHelper(grid, r1 + 1, c1, r2, dp), cherryHelper(grid, r1, c1 + 1, r2, dp))
            
            dp[r1][c1][r2] = result
            return result
        
        n = len(grid)
        dp = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]
        return max(0, cherryHelper(grid, 0, 0, 0, dp))
