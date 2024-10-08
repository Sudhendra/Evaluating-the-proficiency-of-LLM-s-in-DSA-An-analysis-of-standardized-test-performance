from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        dp = triangle[-1]

        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[row][i]

        return dp[0]
