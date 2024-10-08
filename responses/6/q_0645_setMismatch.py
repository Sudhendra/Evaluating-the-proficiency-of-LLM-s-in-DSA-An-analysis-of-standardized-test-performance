from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        duplicate = sum(nums) - sum(set(nums))
        missing = expected_sum - actual_sum + duplicate
        return [duplicate, missing]
