from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_count = nums.count(0)
        nums[:] = [num for num in nums if num != 0] + [0] * zero_count
