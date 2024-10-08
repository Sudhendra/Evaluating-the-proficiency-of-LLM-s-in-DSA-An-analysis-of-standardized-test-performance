class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1
        dp[0][1] = 1
        dp[1][0] = 1
        
        for i in range(1, n):
            new_dp = [[0] * 3 for _ in range(2)]
            new_dp[0][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % MOD
            new_dp[0][1] = dp[0][0]
            new_dp[0][2] = dp[0][1]
            new_dp[1][0] = (dp[0][0] + dp[0][1] + dp[0][2] + dp[1][0] + dp[1][1] + dp[1][2]) % MOD
            
            dp = new_dp
        
        return sum(dp[0] + dp[1]) % MOD
