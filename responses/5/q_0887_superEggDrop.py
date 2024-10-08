class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for m in range(1, n + 1):
            for eggs in range(1, k + 1):
                dp[m][eggs] = dp[m - 1][eggs - 1] + dp[m - 1][eggs] + 1
                if dp[m][eggs] >= n:
                    return m
