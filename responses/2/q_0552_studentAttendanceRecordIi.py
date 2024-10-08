class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0, 0, 0], [0, 0, 0]]  # Represents number of records with length 1
        dp[0][0] = dp[1][0] = dp[0][1] = 1

        for _ in range(2, n+1):
            new_dp = [[0, 0, 0], [0, 0, 0]]
            
            new_dp[0][0] = sum(dp[0]) % MOD  # Number of records ending with 'P'
            new_dp[0][1] = dp[0][0] % MOD     # Number of records ending with 'L'
            new_dp[0][2] = (sum(dp[1]) + dp[0][1]) % MOD     # Number of records ending with 'A'

            new_dp[1][0] = sum(dp[1]) % MOD  # Number of records ending with 'PP'
            new_dp[1][1] = dp[1][0] % MOD    # Number of records ending with 'PL'
            new_dp[1][2] = dp[1][1] % MOD    # Number of records ending with 'PA'
            
            dp = new_dp

        return sum(sum(row) for row in dp) % MOD