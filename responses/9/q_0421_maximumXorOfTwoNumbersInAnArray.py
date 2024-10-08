from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        result = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            prefixSet = set([num & mask for num in nums])
            candidate = result | 1 << i
            for prefix in prefixSet:
                if candidate ^ prefix in prefixSet:
                    result = candidate
                    break
        return result
