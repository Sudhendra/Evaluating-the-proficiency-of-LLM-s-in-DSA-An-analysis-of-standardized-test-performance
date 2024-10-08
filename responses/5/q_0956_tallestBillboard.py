from typing import List

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        memo = {}

        def dp(i, s):
            if i == len(rods):
                return 0 if s == 0 else float('-inf')
            if (i, s) in memo:
                return memo[(i, s)]

            # choose to add rod[i] to left subset
            add_left = dp(i + 1, s + rods[i]) + rods[i]

            # choose to add rod[i] to right subset
            add_right = dp(i + 1, s - rods[i])

            # skip rod[i]
            skip = dp(i + 1, s)

            # return maximum height when considering the current rod
            memo[(i, s)] = max(add_left, add_right, skip)

            return memo[(i, s)]

        return dp(0, 0)
