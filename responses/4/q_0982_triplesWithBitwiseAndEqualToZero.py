from typing import List

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        count = [0] * (2**16)
        for num1 in nums:
            for num2 in nums:
                count[num1 & num2] += 1
        
        res = 0
        for num in nums:
            for i in range(2**16):
                if num & i == 0:
                    res += count[i]
        
        return res