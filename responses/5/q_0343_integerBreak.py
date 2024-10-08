class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n+1)  # dp[i] stores the max product of breaking number i
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n+1):
            max_product = 0
            for j in range(1, i // 2 + 1):
                max_product = max(max_product, dp[j] * dp[i - j])
            dp[i] = max_product

        return dp[n]
