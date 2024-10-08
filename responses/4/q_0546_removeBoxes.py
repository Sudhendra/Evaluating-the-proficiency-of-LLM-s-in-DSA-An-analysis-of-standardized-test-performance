from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        memo = dict()

        def dp(l, r, k):
            if l > r:
                return 0

            if (l, r, k) in memo:
                return memo[(l, r, k)]

            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1

            result = dp(l, r - 1, 0) + (k + 1) * (k + 1)

            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    result = max(result, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))

            memo[(l, r, k)] = result
            return result

        return dp(0, n - 1, 0)
