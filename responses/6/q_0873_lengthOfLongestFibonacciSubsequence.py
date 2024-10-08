from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        indices = {x: i for i, x in enumerate(arr)}
        dp = {}
        longest = 0
        for k in range(len(arr)):
            for j in range(k):
                i = indices.get(arr[k] - arr[j], -1)
                if i >= 0 and i < j:
                    dp[j, k] = dp.get((i, j), 2) + 1
                    longest = max(longest, dp[j, k])
        return longest if longest > 2 else 0
