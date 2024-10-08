class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        directions = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
        
        for i in range(n):
            for j in range(n):
                dp[0][i][j] = 1
        
        for s in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n:
                            dp[s][i][j] += dp[s-1][x][y] / 8
                            
        return sum([sum(row) for row in dp[k]])