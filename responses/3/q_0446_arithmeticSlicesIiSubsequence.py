from collections import defaultdict
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        dp = [defaultdict(int) for _ in nums]
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                total += dp[j][diff]
                dp[i][diff] += dp[j][diff] + 1
        return total
