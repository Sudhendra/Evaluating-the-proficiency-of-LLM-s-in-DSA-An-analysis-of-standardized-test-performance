from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}  # Key: (index, difference), Value: length of longest arithmetic subsequence ending at index with difference
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
        return max(dp.values())
