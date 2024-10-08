from functools import lru_cache

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        
        @lru_cache(None)
        def dp(x, y, k):
            if k == 0:
                return 1 if 0 <= x < n and 0 <= y < n else 0
            prob = 0
            for dx, dy in moves:
                newX, newY = x + dx, y + dy
                if 0 <= newX < n and 0 <= newY < n:
                    prob += dp(newX, newY, k - 1) / 8
            return prob
        
        return dp(row, column, k)
