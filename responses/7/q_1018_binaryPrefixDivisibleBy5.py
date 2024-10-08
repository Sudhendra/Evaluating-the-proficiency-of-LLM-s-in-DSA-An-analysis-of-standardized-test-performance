from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        num = 0
        for i in nums:
            num = (num * 2 + i) % 5
            result.append(num == 0)
        return result
