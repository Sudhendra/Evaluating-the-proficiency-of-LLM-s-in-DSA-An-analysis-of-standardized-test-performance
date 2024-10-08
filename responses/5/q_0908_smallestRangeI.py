from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)

        diff = max_num - min_num - 2*k
        return max(diff, 0)
