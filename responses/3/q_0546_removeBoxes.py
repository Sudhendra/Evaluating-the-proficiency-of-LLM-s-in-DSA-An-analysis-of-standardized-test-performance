from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        memo = [[[0]*n for _ in range(n)] for _ in range(n)]

        def dp(i, j, k):
            if i > j:
                return 0
            if memo[i][j][k] > 0:
                return memo[i][j][k]

            while j > i and boxes[j] == boxes[j-1]:
                j -= 1
                k += 1

            result = dp(i, j-1, 0) + (k+1) * (k+1)

            for m in range(i, j):
                if boxes[m] == boxes[j]:
                    result = max(result, dp(i, m, k+1) + dp(m+1, j-1, 0))

            memo[i][j][k] = result
            return result

        return dp(0, n-1, 0)
