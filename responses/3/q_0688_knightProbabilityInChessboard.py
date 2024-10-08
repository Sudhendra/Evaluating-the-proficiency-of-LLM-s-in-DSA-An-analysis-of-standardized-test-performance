class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1

        for _ in range(k):
            dp_next = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for dr, dc in directions:
                        if 0 <= r + dr < n and 0 <= c + dc < n:
                            dp_next[r + dr][c + dc] += dp[r][c] / 8
            dp = dp_next

        return sum(map(sum, dp))
