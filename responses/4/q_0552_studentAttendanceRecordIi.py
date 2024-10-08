class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 3
        
        dp = [[[0, 0] for _ in range(3)] for _ in range(n)]
        dp[0][0][0] = 1  # P
        dp[0][1][0] = 1  # A
        dp[0][0][1] = 1  # L

        for i in range(1, n):
            for j in range(3):
                dp[i][j][0] = sum(dp[i - 1][l][0] for l in range(3)) % MOD  # ending with P
                if j == 0:
                    dp[i][j][1] = sum(dp[i - 1][l][1] for l in range(3)) % MOD  # ending with L
                dp[i][1][0] = (dp[i][1][0] + dp[i - 1][j][0]) % MOD  # ending with A
        
        total = sum(sum(dp[n - 1][j][k] for k in range(2)) for j in range(3))
        return total % MOD

# Uncomment the line below for testing
# print(Solution().checkRecord(10101))
