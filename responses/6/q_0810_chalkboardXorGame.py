from typing import List

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        # Check if the length of nums is even, if so Alice wins
        return len(nums) % 2 == 0 or not reduce(lambda x, y: x ^ y, nums)
