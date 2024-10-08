from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def is_magic_square(i, j):
            if grid[i+1][j+1] != 5:
                return False
            s = ''.join(str(grid[i+x//3][j+x%3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return grid[i][j] % 2 == 0 and grid[i+2][j+2] % 2 == 0 and s in '43816729,43816729'

        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_magic_square(i, j):
                    count += 1

        return count
