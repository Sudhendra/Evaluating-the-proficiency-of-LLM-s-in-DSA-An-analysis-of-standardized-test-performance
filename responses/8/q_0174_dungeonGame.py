from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[m][n-1] = dp[m-1][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        
        return dp[0][0]

# Instantiate the Solution class
sol = Solution()

# Test the function with the provided examples
print(sol.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))  # Output: 7
print(sol.calculateMinimumHP([[0]]))  # Output: 1
