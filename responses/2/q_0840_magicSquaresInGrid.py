from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_square(subgrid):
            s = set()
            for i in range(3):
                for j in range(3):
                    if subgrid[i][j] < 1 or subgrid[i][j] > 9 or subgrid[i][j] in s:
                        return False
                    s.add(subgrid[i][j])
            if sum(subgrid[0]) == sum(subgrid[1]) == sum(subgrid[2]) == sum(subgrid[i][0] for i in range(3)) == sum(subgrid[i][1] for i in range(3)) == sum(subgrid[i][2] for i in range(3)) == sum(subgrid[i][i] for i in range(3)) == sum(subgrid[i][2-i] for i in range(3)) == 15:
                return True
            return False

        count = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                subgrid = [row[j:j+3] for row in grid[i:i+3]]
                if is_magic_square(subgrid):
                    count += 1
        return count
