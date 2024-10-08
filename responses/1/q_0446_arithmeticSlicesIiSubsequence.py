from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        dp = [{} for _ in nums]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                prev_count = dp[j].get(diff, 0)
                current_count = dp[i].get(diff, 0)
                
                current_count += prev_count + 1
                dp[i][diff] = current_count
                total += prev_count
                
        return total