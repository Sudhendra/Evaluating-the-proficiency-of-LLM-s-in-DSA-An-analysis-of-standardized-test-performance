from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0
        
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        for i in range(n):
            left[i][0] = grid[i][0]
            right[i][n-1] = grid[i][n-1]
            up[0][i] = grid[0][i]
            down[n-1][i] = grid[n-1][i]

        for i in range(n):
            for j in range(1, n):
                left[i][j] = left[i][j-1] + grid[i][j] if grid[i][j] else 0
                right[i][n-1-j] = right[i][n-j] + grid[i][n-1-j] if grid[i][n-1-j] else 0
                up[j][i] = up[j-1][i] + grid[j][i] if grid[j][i] else 0
                down[n-1-j][i] = down[n-j][i] + grid[n-1-j][i] if grid[n-1-j][i] else 0

        result = 0
        for i in range(n):
            for j in range(n):
                result = max(result, min(left[i][j], right[i][j], up[i][j], down[i][j]))
        
        return result
