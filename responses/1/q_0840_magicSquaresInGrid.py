from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(square):
            nums = set(square)
            if nums != set(range(1, 10)):
                return False

            if square[4] != 5:
                return False

            return (square[0] + square[1] + square[2] == 15 and
                    square[3] + square[4] + square[5] == 15 and
                    square[6] + square[7] + square[8] == 15 and
                    square[0] + square[3] + square[6] == 15 and
                    square[1] + square[4] + square[7] == 15 and
                    square[2] + square[5] + square[8] == 15 and
                    square[0] + square[4] + square[8] == 15 and
                    square[2] + square[4] + square[6] == 15)

        def get_subgrid(i, j):
            return [grid[i+k][j:j+3] for k in range(3)]

        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                subgrid = get_subgrid(i, j)
                if is_magic([num for row in subgrid for num in row]):
                    count += 1

        return count
