class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)
        max_row_values = [max(row) for row in grid]
        max_col_values = [max([grid[i][j] for i in range(n)]) for j in range(n)]

        total_increase = 0
        for i in range(n):
            for j in range(n):
                total_increase += min(max_row_values[i], max_col_values[j]) - grid[i][j]

        return total_increase