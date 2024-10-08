class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        
        MOD = 10**9 + 7
        dp = [[0, 0, 0], [0, 0, 0]]  # DP array to store count of records ending with different characters

        dp[0][0] = 1  # Records ending with 'P'
        dp[0][1] = 1  # Records ending with 'L'
        dp[0][2] = 0  # Records ending with 'A'

        for _ in range(1, n):
            dp[1][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % MOD  # New records ending with 'P'
            dp[1][1] = dp[0][0]  # New records ending with 'L'

            dp[1][2] = (dp[0][0] + dp[0][1] + dp[0][2]) % MOD  # New records ending with 'A'
            dp[1][2] = (dp[1][2] + dp[0][2]) % MOD

            dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]

        return sum(dp[1]) % MOD