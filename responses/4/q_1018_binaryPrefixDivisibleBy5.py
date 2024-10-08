from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        num = 0
        for i in nums:
            num = (num << 1) + i
            result.append(num % 5 == 0)
        return result
