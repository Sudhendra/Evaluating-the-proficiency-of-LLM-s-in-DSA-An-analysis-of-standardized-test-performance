class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
        dp = [[0, 0, 0], [0, 0, 0]]  # dp[i][j]: number of records of length i meeting condition j
        dp[0][0] = 1

        for i in range(1, n+1):
            new_dp = [[0, 0, 0], [0, 0, 0]]
            # calculate records ending with 'P'
            for j in range(0, 3):
                new_dp[0][j] = sum(dp[0]) % MOD
                
            # calculate records ending with 'A'
            for j in range(0, 2):
                new_dp[1][j] = sum(dp[1]) % MOD
            new_dp[1][2] = sum(dp[0]) % MOD

            dp = new_dp

        return sum(sum(row) for row in dp) % MOD
