from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Get the XOR of the two unique numbers
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # Find the rightmost set bit in xor_all
        rightmost_set_bit = xor_all & -xor_all
        
        # Partition the nums into two groups based on the rightmost set bit
        unique_num1 = unique_num2 = 0
        for num in nums:
            if num & rightmost_set_bit:
                unique_num1 ^= num
            else:
                unique_num2 ^= num
        
        return [unique_num1, unique_num2]
