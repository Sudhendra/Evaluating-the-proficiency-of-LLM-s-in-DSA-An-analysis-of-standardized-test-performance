from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_result = 0
        for num in nums:
            xor_result ^= num
        
        # Find the rightmost set bit in xor_result
        rightmost_set_bit = xor_result & -xor_result
        
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]
