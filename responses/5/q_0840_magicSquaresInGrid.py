from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(square):
            s = set(x for row in square for x in row)
            if s != set(range(1, 10)):
                return False
            return all(row_sum == 15 for row_sum in map(sum, square)) and all(col_sum == 15 for col_sum in map(sum, zip(*square))) \
                   and sum(square[i][i] for i in range(3)) == 15 and sum(square[i][2 - i] for i in range(3)) == 15
          
        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                subgrid = [row[j:j+3] for row in grid[i:i+3]]
                if is_magic(subgrid):
                    count += 1
        return count
