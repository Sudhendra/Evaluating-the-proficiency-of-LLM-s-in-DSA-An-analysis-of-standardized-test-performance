from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_square(subgrid):
            if subgrid[1][1] != 5:
                return False
            for i in range(3):
                for j in range(3):
                    if subgrid[i][j] < 1 or subgrid[i][j] > 9:
                        return False
                    if (i == 1 and j == 1) or subgrid[i][j] % 2 == 0:
                        return False
            if subgrid[0][0] + subgrid[2][2] != 10 or subgrid[0][2] + subgrid[2][0] != 10:
                return False
            row_sums = [sum(subgrid[i]) for i in range(3)]
            col_sums = [sum(subgrid[i][j] for i in range(3)) for j in range(3)]
            return set(row_sums + col_sums) == {15}

        rows, cols = len(grid), len(grid[0])
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                subgrid = [[grid[i+x][j+y] for y in range(3)] for x in range(3)]
                if is_magic_square(subgrid):
                    count += 1
        return count
