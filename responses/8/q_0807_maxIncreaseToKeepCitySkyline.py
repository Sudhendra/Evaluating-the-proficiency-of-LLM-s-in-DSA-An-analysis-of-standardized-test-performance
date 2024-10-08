from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_row = [max(row) for row in grid]
        max_col = [max(col) for col in zip(*grid)]

        max_increase = 0
        for i in range(n):
            for j in range(n):
                max_increase += min(max_row[i], max_col[j]) - grid[i][j]

        return max_increase
