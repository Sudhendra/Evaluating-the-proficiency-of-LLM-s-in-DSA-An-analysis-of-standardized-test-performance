from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2] if len(nums) % 2 == 1 else (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) // 2
        return sum(abs(num - median) for num in nums)