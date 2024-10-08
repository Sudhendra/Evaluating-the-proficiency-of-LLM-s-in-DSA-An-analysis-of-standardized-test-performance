from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        
        for i in range(32):  # Considering each bit position from 0 to 31
            count_ones = 0
            for num in nums:
                if (num >> i) & 1:
                    count_ones += 1
            result += count_ones * (n - count_ones)
        
        return result
