from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        def dp(left, right, k):
            if left > right:
                return 0
            
            while right > left and boxes[right] == boxes[right - 1]:
                right -= 1
                k += 1
            
            key = (left, right, k)
            if key in memo:
                return memo[key]
            
            memo[key] = dp(left, right - 1, 0) + (k + 1) ** 2
            
            for i in range(left, right):
                if boxes[i] == boxes[right]:
                    memo[key] = max(memo[key], dp(left, i, k + 1) + dp(i + 1, right - 1, 0))
            
            return memo[key]
        
        memo = {}
        return dp(0, len(boxes) - 1, 0)