class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n + 1)
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n + 1):
            dp[i] = max(2 * dp[i - 2], 3 * dp[i - 3])

        return dp[n]