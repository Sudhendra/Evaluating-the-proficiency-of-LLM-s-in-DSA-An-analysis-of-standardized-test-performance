from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        memo = {}

        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]

            longest = 1
            for dx, dy in dirs:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    longest = max(longest, 1 + dfs(new_row, new_col))

            memo[(row, col)] = longest
            return longest

        result = 0
        for i in range(rows):
            for j in range(cols):
                result = max(result, dfs(i, j))

        return result
