from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @lru_cache(None)
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1 == c1 == r2:
                return grid[r1][c1]
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            cherries = grid[r1][c1]
            if r1 != r2:
                cherries += grid[r2][c2]
            cherries += max(
                dp(r1+1, c1, r2+1),
                dp(r1, c1+1, r2+1),
                dp(r1+1, c1, r2),
                dp(r1, c1+1, r2)
            )
            return cherries

        return max(0, dp(0, 0, 0))
