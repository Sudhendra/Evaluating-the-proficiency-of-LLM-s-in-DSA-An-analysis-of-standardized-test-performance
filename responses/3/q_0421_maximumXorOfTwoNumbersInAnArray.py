from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            prefixes = set()
            for num in nums:
                prefixes.add(num & mask)
            
            possible_max = max_xor | (1 << i)
            for prefix in prefixes:
                if possible_max ^ prefix in prefixes:
                    max_xor = possible_max
                    break
        
        return max_xor