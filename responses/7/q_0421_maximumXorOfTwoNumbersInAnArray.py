from typing import List

class Solution:
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            prefixes = set([num & mask for num in nums])
            temp = ans | (1 << i)
            for prefix in prefixes:
                if temp ^ prefix in prefixes:
                    ans = temp
                    break
        return ans
