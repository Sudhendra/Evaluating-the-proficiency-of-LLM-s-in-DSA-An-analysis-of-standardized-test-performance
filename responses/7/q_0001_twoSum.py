from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

# Example usage:
# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
# print(sol.twoSum([3, 2, 4], 6))  # Output: [1, 2]
# print(sol.twoSum([3, 3], 6))  # Output: [0, 1]
