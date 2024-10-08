from typing import List

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        return xor_sum == 0 or len(nums) % 2 == 0
