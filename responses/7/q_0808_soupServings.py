class Solution:

    def soupServings(self, N: int) -> float:
        N = (N + 24) // 25
        if N > 500:
            return 1
        dp = [[0.0] * (N + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            for j in range(N + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0.5
                elif i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 0.25 * (dp[max(i - 4, 0)][j] +
                                      dp[max(i - 3, 0)][max(j - 1, 0)] +
                                      dp[max(i - 2, 0)][max(j - 2, 0)] +
                                      dp[max(i - 1, 0)][max(j - 3, 0)])
        return dp[N][N]
