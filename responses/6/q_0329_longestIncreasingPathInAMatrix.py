from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(x, y) if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > val else 0
                    for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)
                )
            return dp[i][j]

        longest_path = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest_path = max(longest_path, dfs(i, j))
        
        return longest_path
