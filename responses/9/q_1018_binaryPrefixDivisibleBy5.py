from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        x = 0
        for num in nums:
            x = (x * 2 + num) % 5
            result.append(x == 0)
        return result
