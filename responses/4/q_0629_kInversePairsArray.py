class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[1][0] = 1

        for i in range(2, n + 1):
            dp[i][0] = 1
            for j in range(1, k + 1):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
                if j >= i:
                    dp[i][j] = (dp[i][j] - dp[i-1][j-i] + MOD) % MOD

        return dp[n][k]
