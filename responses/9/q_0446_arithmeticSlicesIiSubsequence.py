from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total_count = 0
        dp = [defaultdict(int) for _ in nums]
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                count_j = dp[j][diff]
                dp[i][diff] += count_j + 1
                total_count += count_j
                
        return total_count

# Additional solutions can be added as methods of the same class
