from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        
        diff = max_val - min_val - 2*k
        return max(diff, 0)
