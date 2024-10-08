from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        n = len(nums)
        
        for i in range(32):
            count_set_bits = 0
            for num in nums:
                count_set_bits += (num >> i) & 1
            
            total_distance += count_set_bits * (n - count_set_bits)
        
        return total_distance
