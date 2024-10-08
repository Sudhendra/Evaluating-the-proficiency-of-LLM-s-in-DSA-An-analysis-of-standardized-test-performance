class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        
        directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        
        for i in range(n):
            for j in range(n):
                dp[0][i][j] = 1
        
        for s in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    prob = 0
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            prob += dp[s-1][ni][nj]
                    dp[s][i][j] = prob / 8
        
        res = 0
        for i in range(n):
            for j in range(n):
                res += dp[k][i][j]
        
        return res
