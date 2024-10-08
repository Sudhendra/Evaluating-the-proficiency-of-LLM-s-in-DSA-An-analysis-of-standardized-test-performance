class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]

        def calculatePoints(boxes, dp, i, j, k):
            if i > j:
                return 0
            if dp[i][j][k] != 0:
                return dp[i][j][k]

            while i < j and boxes[j] == boxes[j - 1]:
                j -= 1
                k += 1

            dp[i][j][k] = calculatePoints(boxes, dp, i, j - 1, 0) + (k + 1) * (k + 1)

            for p in range(i, j):
                if boxes[p] == boxes[j]:
                    dp[i][j][k] = max(dp[i][j][k], calculatePoints(boxes, dp, i, p, k + 1) + calculatePoints(boxes, dp, p + 1, j - 1, 0))

            return dp[i][j][k]

        return calculatePoints(boxes, dp, 0, n - 1, 0)