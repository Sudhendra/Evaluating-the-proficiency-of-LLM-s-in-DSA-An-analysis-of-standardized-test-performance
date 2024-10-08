from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(set(nums))
        duplicate_num = sum(nums) - actual_sum
        missing_num = total_sum - actual_sum
        return [duplicate_num, missing_num]