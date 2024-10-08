from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = n * (n + 1) // 2
        duplicated = sum(nums) - sum(set(nums))
        missing = total - sum(set(nums))
        return [duplicated, missing]
