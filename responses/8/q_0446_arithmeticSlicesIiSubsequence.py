from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        cnt = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[i].get(diff, 0) + dp[j][diff]
                    cnt += dp[j][diff]
                    dp[i][diff] += 1
                else:
                    dp[i][diff] = dp[i].get(diff, 0) + 1
        
        return cnt

# Example usage
solution = Solution()
print(solution.numberOfArithmeticSlices([2, 4, 6, 8, 10]))  # Output: 7
print(solution.numberOfArithmeticSlices([7, 7, 7, 7, 7]))  # Output: 16
