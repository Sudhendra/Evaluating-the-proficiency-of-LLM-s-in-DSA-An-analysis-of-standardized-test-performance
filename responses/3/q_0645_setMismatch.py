from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual_sum = sum(nums)
        expected_sum = n * (n + 1) // 2
        duplicate = actual_sum - sum(set(nums))
        missing = expected_sum - actual_sum + duplicate
        return [duplicate, missing]
