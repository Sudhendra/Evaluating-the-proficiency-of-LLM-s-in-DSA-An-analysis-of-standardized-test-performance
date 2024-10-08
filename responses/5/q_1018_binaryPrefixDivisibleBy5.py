from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        num = 0
        for n in nums:
            num = (num << 1) | n
            result.append(num % 5 == 0)
        return result
