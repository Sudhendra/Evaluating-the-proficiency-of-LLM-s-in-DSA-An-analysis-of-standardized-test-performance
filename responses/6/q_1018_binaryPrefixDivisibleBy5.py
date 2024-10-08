from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        curr_num = 0
        for num in nums:
            curr_num = (curr_num * 2 + num) % 5
            result.append(curr_num == 0)
        return result
