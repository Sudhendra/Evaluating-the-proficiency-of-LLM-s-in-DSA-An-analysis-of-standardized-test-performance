class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        mod_val = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        dp[3] = 5
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % mod_val
        return dp[n]