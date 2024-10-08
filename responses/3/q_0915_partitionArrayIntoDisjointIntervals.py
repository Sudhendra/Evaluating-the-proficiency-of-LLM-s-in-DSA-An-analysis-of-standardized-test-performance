from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max_left = min_right = nums[0]
        partition_idx = 0
        max_seen = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < max_left:
                partition_idx = i
                max_left = max_seen
            else:
                max_seen = max(max_seen, nums[i])
        
        return partition_idx + 1
