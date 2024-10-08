from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        return sum(num - min_num for num in nums)
