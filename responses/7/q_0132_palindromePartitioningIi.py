class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return 0

        dp = [i - 1 for i in range(n + 1)]
        for i in range(1, n):
            for j in range(i + 1):
                if s[j:i] == s[j:i][::-1]:
                    dp[i + 1] = min(dp[i + 1], dp[j] + 1)

        return dp[n]
