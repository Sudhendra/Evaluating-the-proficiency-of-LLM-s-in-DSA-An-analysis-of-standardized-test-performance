from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(square):
            s = set(square)
            if s != set(range(1, 10)):
                return False
            row_sums = [sum(square[i:i+3]) for i in range(0, 9, 3)]
            col_sums = [sum(square[i::3]) for i in range(3)]
            diag1_sum = sum(square[::4])
            diag2_sum = sum(square[2:7:2])
            return row_sums[0] == row_sums[1] == row_sums[2] == col_sums[0] == col_sums[1] == col_sums[2] == diag1_sum == diag2_sum

        def get_square(i, j):
            return [grid[i+k][j+l] for k in range(3) for l in range(3)]

        rows, cols = len(grid), len(grid[0])
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                square = get_square(i, j)
                if is_magic(square):
                    count += 1

        return count
