from typing import List

class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {}
        
        for i, num in enumerate(nums):
            if num in num_map and abs(i - num_map[num]) <= k:
                return True
            num_map[num] = i
        
        return False
