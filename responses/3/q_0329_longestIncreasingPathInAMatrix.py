from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(row, col):
            if dp[row][col] != 0:
                return dp[row][col]

            max_path = 1
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    max_path = max(max_path, 1 + dfs(new_row, new_col))

            dp[row][col] = max_path
            return max_path

        result = 0
        for i in range(rows):
            for j in range(cols):
                result = max(result, dfs(i, j))

        return result
