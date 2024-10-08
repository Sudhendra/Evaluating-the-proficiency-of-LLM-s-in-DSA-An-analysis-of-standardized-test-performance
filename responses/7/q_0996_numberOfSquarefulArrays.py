from typing import List

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(num):
            return int(num ** 0.5) ** 2 == num
        
        def dfs(remaining_nums, prev_num):
            if not remaining_nums:
                return 1
            
            total = 0
            for i, num in enumerate(remaining_nums):
                if i > 0 and remaining_nums[i] == remaining_nums[i - 1]:
                    continue
                if not prev_num or is_square(prev_num + num):
                    total += dfs(remaining_nums[:i] + remaining_nums[i+1:], num)
            
            return total
        
        nums.sort()
        return dfs(nums, None)

# Sample usages
solution = Solution()
print(solution.numSquarefulPerms([1, 17, 8]))  # Output: 2
print(solution.numSquarefulPerms([2, 2, 2]))  # Output: 1
