class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        def dfs(i, j):
            if i > j:
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            while j > i and s[j] == s[j - 1]:
                j -= 1
            dp[i][j] = dfs(i, j - 1) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    dp[i][j] = min(dp[i][j], dfs(i, k) + dfs(k + 1, j - 1))
            return dp[i][j]

        return dfs(0, n - 1)