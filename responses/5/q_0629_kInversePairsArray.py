class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[1][0] = 1
        for i in range(2, n + 1):
            dp[i][0] = 1
            for j in range(1, k + 1):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % mod
                if j >= i:
                    dp[i][j] = (dp[i][j] - dp[i - 1][j - i]) % mod
        return (dp[n][k] - dp[n][k - 1]) % mod
