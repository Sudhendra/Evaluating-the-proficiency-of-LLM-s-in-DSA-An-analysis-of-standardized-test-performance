class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3

        MOD = 10**9 + 7
        dp = [[0, 0, 0], [0, 0, 0]]  # dp[i][j] represents the number of records of length i with j absent and ending with 0, 1, 2 continuous 'L's

        dp[1][0] = 1
        dp[1][1] = 1
        dp[1][2] = 0

        for i in range(2, n + 1):
            newDp = [[0, 0, 0], [0, 0, 0]]
            newDp[0][0] = sum(dp[1]) % MOD  # ending with 'P'
            newDp[1][0] = dp[0][0]  # ending with 'A'

            newDp[0][1] = dp[0][0]  # ending with 'L'
            newDp[1][1] = dp[1][0]  # ending with 'A'

            newDp[0][2] = sum(dp[0]) % MOD  # ending with 'LL'
            newDp[1][2] = dp[1][1]  # ending with 'AL'

            dp = newDp

        return sum(map(sum, dp)) % MOD
