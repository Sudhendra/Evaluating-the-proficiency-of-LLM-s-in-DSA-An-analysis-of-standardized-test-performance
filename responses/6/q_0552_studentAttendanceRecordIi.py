class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 3
        dp = [[0, 0, 0], [0, 0, 0]]  # dp[i][j] represents the number of valid records of length i where the student had j consecutive 'L's
        dp[0][0] = 1
        dp[1][0] = 1
        dp[1][1] = 1

        for i in range(2, n + 1):
            new_dp = [[0, 0, 0], [0, 0, 0]]
            new_dp[0][0] = sum(dp[0]) % MOD  # Ends with P
            new_dp[1][0] = dp[0][0] % MOD  # Ends with A
            new_dp[0][1] = dp[0][0] % MOD  # Ends with PL
            new_dp[0][2] = dp[0][1] % MOD  # Ends with LL
            new_dp[1][1] = dp[1][0] % MOD  # Ends with AL
            new_dp[1][2] = dp[1][1] % MOD  # Ends with LA

            dp = new_dp

        return sum(map(sum, dp)) % MOD
