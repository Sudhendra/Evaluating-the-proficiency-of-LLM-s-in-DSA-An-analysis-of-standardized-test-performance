from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        mask = 1
        while mask & xor == 0:
            mask <<= 1
        
        num1, num2 = 0, 0
        for num in nums:
            if num & mask:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]