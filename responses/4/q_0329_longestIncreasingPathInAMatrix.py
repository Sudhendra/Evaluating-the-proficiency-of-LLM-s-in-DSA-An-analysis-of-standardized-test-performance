from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        def dfs(i, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]

            max_path = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                    max_path = max(max_path, 1 + dfs(x, y, memo))

            memo[(i, j)] = max_path
            return max_path

        memo = {}
        max_length = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0]):
                max_length = max(max_length, dfs(i, j, memo))

        return max_length
