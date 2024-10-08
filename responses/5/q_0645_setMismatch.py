from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(set(nums))
        duplicate = sum(nums) - actual_sum
        missing = total_sum - actual_sum
        return [duplicate, missing]
