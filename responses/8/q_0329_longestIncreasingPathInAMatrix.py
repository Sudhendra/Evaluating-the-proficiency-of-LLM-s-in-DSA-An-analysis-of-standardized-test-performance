from typing import List

class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        memo = [[0]*n for _ in range(m)]
        
        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]
            
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    memo[i][j] = max(memo[i][j], dfs(x, y))
                    
            memo[i][j] += 1
            return memo[i][j]
        
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        
        return result
