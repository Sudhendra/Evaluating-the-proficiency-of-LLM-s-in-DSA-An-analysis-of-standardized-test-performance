from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        max_weight = total_sum // 2
        dp = [False] * (max_weight + 1)
        dp[0] = True

        for stone in stones:
            for j in range(max_weight, stone - 1, -1):
                dp[j] |= dp[j - stone]

        for i in range(max_weight, -1, -1):
            if dp[i]:
                return total_sum - 2 * i

        return total_sum
