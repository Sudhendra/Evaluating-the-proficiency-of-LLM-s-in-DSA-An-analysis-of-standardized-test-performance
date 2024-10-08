from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(square):
            s = set(square)
            return (len(s) == 9 and
                    all(1 <= x <= 9 for x in s) and
                    square[0] + square[1] + square[2] == square[3] + square[4] + square[5] ==
                    square[6] + square[7] + square[8] == square[0] + square[3] + square[6] ==
                    square[1] + square[4] + square[7] == square[2] + square[5] + square[8] ==
                    square[0] + square[4] + square[8] == square[2] + square[4] + square[6])

        def subgrid_sum(i, j):
            return grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]

        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if grid[i + 1][j + 1] == 5:
                    if is_magic([grid[i][j], grid[i][j + 1], grid[i][j + 2],
                                 grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                                 grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]]):
                        count += 1

        return count
