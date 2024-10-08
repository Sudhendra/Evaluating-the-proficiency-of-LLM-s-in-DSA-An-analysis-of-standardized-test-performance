from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        dp = [False] * ((total_sum // 2) + 1)
        dp[0] = True

        for stone in stones:
            for i in range(len(dp) - 1, -1, -1):
                if i >= stone:
                    dp[i] = dp[i] or dp[i - stone]

        for i in range(len(dp) // 2, -1, -1):
            if dp[i]:
                return total_sum - 2 * i

        return total_sum
