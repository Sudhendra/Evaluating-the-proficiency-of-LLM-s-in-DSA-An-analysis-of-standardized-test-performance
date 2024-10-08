from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = set((x, y) for x, y in mines)  # Convert mines to a set for O(1) lookup
        grid = [[n] * n for _ in range(n)]  # Initialize grid with max possible order of plus sign

        for i in range(n):
            left, right, up, down = 0, 0, 0, 0  # Initialize counts for directions
            for j in range(n):
                left = 0 if (i, j) in banned else left + 1
                grid[i][j] = min(grid[i][j], left)

                right = 0 if (i, n - 1 - j) in banned else right + 1
                grid[i][n - 1 - j] = min(grid[i][n - 1 - j], right)

                up = 0 if (j, i) in banned else up + 1
                grid[j][i] = min(grid[j][i], up)

                down = 0 if (n - 1 - j, i) in banned else down + 1
                grid[n - 1 - j][i] = min(grid[n - 1 - j][i], down)

        res = 0
        for i in range(n):
            for j in range(n):
                res = max(res, grid[i][j])

        return res
