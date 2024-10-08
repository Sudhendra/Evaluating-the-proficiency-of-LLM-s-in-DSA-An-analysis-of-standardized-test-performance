class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dp = [[0] * cols for _ in range(rows)]
        
        def dfs(row, col):
            if dp[row][col] != 0:
                return dp[row][col]
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    dp[row][col] = max(dp[row][col], dfs(new_row, new_col))
            
            dp[row][col] += 1
            return dp[row][col]
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))
        
        return res