from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing = 1
        added = 0
        i = 0

        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                missing += missing
                added += 1

        return added
