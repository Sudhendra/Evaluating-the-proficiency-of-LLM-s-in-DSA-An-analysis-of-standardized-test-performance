from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for idx, num in enumerate(nums):
            if num in seen and idx - seen[num] <= k:
                return True
            seen[num] = idx
        return False
