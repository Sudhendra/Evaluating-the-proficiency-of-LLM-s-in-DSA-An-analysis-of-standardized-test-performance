class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (goal + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, goal + 1):
                dp[i][j] = (dp[i-1][j-1] * (n - (i - 1)) + dp[i][j-1] * max(i - k, 0)) % mod
        
        return dp[n][goal]
