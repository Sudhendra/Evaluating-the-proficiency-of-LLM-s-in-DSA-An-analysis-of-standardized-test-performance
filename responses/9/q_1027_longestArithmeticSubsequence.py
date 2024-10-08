from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = defaultdict(int)
        n = len(nums)
        longest = 2

        for i in range(n):
            for j in range(i + 1, n):
                diff = nums[j] - nums[i]
                if (i, diff) in dp:
                    dp[j, diff] = dp[i, diff] + 1
                else:
                    dp[j, diff] = 2
                longest = max(longest, dp[j, diff])

        return longest
