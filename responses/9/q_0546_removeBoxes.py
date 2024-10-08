class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]

        def helper(i, j, k):
            if i > j:
                return 0
            if dp[i][j][k] > 0:
                return dp[i][j][k]

            while j > i and boxes[j] == boxes[j-1]:
                j -= 1
                k += 1

            points = helper(i, j-1, 0) + (k + 1) * (k + 1)

            for m in range(i, j):
                if boxes[m] == boxes[j]:
                    points = max(points, helper(i, m, k+1) + helper(m+1, j-1, 0))

            dp[i][j][k] = points
            return points

        return helper(0, n-1, 0)
