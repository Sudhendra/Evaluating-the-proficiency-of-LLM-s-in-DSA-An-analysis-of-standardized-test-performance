from typing import List

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0 or not any(nums):
            return True
        xored = 0
        for num in nums:
            xored ^= num
        return xored == 0
