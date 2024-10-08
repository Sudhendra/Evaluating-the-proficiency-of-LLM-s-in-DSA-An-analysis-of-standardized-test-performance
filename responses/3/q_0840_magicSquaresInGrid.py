from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic_square(grid, i, j):
            if grid[i + 1][j + 1] != 5:
                return False
            s = ''.join(str(grid[i + x // 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return re.match('123456789', s) and all([int(s[i]) < int(s[i + 1]) for i in range(8)])
        
        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if is_magic_square(grid, i, j):
                    count += 1
        return count
