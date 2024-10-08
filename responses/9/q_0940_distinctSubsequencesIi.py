class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        dp = [0] * (len(s) + 1)
        last = {}
        dp[0] = 1

        for i in range(1, len(s) + 1):
            dp[i] = (2 * dp[i - 1]) % mod
            if s[i - 1] in last:
                dp[i] -= dp[last[s[i - 1]] - 1]
            dp[i] %= mod
            last[s[i - 1]] = i

        return (dp[-1] - 1) % mod
