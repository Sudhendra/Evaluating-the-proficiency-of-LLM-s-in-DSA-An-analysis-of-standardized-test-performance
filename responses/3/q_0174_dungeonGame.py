class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[0] * cols for _ in range(rows)]

        dp[rows - 1][cols - 1] = max(1, 1 - dungeon[rows - 1][cols - 1])

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j == cols - 1:
                    continue
                elif i == rows - 1:
                    dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])
                elif j == cols - 1:
                    dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j])

        return dp[0][0]