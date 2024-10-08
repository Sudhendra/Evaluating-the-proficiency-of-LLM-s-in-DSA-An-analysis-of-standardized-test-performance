class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(2, 1), (1, 2), (-2, 1), (1, -2), (2, -1), (-1, 2), (-2, -1), (-1, -2)]
        
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1
        
        for _ in range(k):
            dp_temp = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc
                        if 0 <= new_r < n and 0 <= new_c < n:
                            dp_temp[new_r][new_c] += dp[r][c] / 8
            dp = dp_temp
        
        return sum(map(sum, dp))
