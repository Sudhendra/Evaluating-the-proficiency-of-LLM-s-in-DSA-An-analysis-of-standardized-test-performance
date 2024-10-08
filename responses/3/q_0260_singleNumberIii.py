from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        diff_bit = xor & (-xor)
        
        group1 = 0
        group2 = 0
        for num in nums:
            if num & diff_bit:
                group1 ^= num
            else:
                group2 ^= num
        
        return [group1, group2]