class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3

        mod = 10**9 + 7
        dp = [[0, 0, 0], [0, 0, 0]]  # Initialize DP array to store count for the last 2 days sequence

        dp[0][0] = 1  # 1 day sequence
        dp[0][1] = 1  # 1 day sequence ending with 'L'
        dp[0][2] = 0  # 1 day sequence ending with 'A'

        for i in range(2, n+1):  # Loop for the days starting from 2 till n
            new_dp = [0, 0, 0]

            # Calculate count of sequences ending with 'P'
            new_dp[0] = (dp[0][0] + dp[0][1] + dp[0][2]) % mod

            # Calculate count of sequences ending with 'L'
            new_dp[1] = dp[0][0]

            # Calculate count of sequences ending with 'A'
            new_dp[2] = (dp[0][0] + dp[0][1]) % mod

            dp[0] = dp[1]
            dp[1] = new_dp

        return sum(dp[1]) % mod