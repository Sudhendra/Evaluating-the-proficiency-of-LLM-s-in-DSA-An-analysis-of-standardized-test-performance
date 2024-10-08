from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0][:]
        
        for i in range(1, n):
            new_dp = [0] * n
            for j in range(n):
                new_dp[j] = matrix[i][j] + min(dp[max(0, j-1):min(n, j+2)])
            dp = new_dp
        
        return min(dp)
