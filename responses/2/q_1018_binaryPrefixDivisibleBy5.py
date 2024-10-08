from typing import List

class Solution:
    
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        prefix = 0
        for num in nums:
            prefix = (prefix << 1) + num
            result.append(prefix % 5 == 0)
        return result
