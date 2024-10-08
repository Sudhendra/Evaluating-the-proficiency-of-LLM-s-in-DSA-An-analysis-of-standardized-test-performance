class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3

        mod = 10**9 + 7
        dp = [[0, 0, 0], [0, 0, 0]]  # Represents counts of valid records ending with 'A', 'L', 'P'

        dp[0][0] = 1  # Represents valid records of length 1
        dp[0][1] = 1
        dp[0][2] = 1

        for i in range(1, n):
            dp[i % 2][0] = (dp[(i - 1) % 2][1] + dp[(i - 1) % 2][2] + dp[(i - 1) % 2][0]) % mod
            dp[i % 2][1] = dp[(i - 1) % 2][0] % mod
            dp[i % 2][2] = (dp[(i - 1) % 2][0] + dp[(i - 1) % 2][1]) % mod

        return sum(dp[(n - 1) % 2]) % mod