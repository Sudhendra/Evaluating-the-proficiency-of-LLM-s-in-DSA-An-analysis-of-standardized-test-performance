from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(lambda: 1)
        max_length = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
                max_length = max(max_length, dp[(i, diff)])

        return max_length
