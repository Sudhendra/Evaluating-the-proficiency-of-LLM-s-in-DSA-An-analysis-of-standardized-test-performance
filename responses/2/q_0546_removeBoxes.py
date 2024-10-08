from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        def dfs(left, right, k):
            if left > right:
                return 0
            while left < right and boxes[left] == boxes[left + 1]:
                left += 1
                k += 1
            res = (k + 1) ** 2 + dfs(left + 1, right, 0)
            for i in range(left + 1, right + 1):
                if boxes[left] == boxes[i]:
                    res = max(res, dfs(left + 1, i - 1, 0) + dfs(i, right, k + 1))
            return res
        
        return dfs(0, len(boxes) - 1, 0)
