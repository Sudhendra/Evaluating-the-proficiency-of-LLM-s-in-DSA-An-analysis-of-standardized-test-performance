class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[row][column] = 1
        
        for _ in range(k):
            new_dp = [[0 for _ in range(n)] for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            new_dp[nr][nc] += dp[r][c] / 8
            dp = new_dp
        
        return sum(map(sum, dp))
