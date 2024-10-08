from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        res = 2
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                if (i, diff) in dp:
                    dp[(j, diff)] = dp[(i, diff)] + 1
                else:
                    dp[(j, diff)] = 2
                res = max(res, dp[(j, diff)])
        return res