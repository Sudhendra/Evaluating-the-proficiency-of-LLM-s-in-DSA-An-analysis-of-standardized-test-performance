from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        
        # dp[l][r][k] represents the maximum points when considering sub-array boxes[l:r+1] with k boxes equal to boxes[r]
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        
        def calculatePoints(boxes, dp, l, r, k):
            if l > r:
                return 0
            if dp[l][r][k] != 0:
                return dp[l][r][k]
            
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            
            dp[l][r][k] = calculatePoints(boxes, dp, l, r - 1, 0) + (k + 1) * (k + 1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    dp[l][r][k] = max(dp[l][r][k], calculatePoints(boxes, dp, l, i, k + 1) + calculatePoints(boxes, dp, i + 1, r - 1, 0))
            
            return dp[l][r][k]
        
        return calculatePoints(boxes, dp, 0, n - 1, 0)
