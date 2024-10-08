from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        current_num = 0
        for num in nums:
            current_num = (current_num << 1) + num
            result.append(current_num % 5 == 0)
        return result
