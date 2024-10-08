from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_square(subgrid):
            s = set(subgrid)
            if s != set(range(1, 10)):
                return False
            for i in range(3):
                if sum(subgrid[i]) != 15 or sum(subgrid[j][i] for j in range(3)) != 15:
                    return False
            return subgrid[0][0] + subgrid[1][1] + subgrid[2][2] == 15 and subgrid[0][2] + subgrid[1][1] + subgrid[2][0] == 15

        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                subgrid = [row[j:j+3] for row in grid[i:i+3]]
                if is_magic_square(subgrid):
                    count += 1
        return count
