from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) == 1:
            return False

        num_index_map = {}

        for i in range(len(nums)):
            if nums[i] in num_index_map and i - num_index_map[nums[i]] <= k:
                return True
            num_index_map[nums[i]] = i

        return False