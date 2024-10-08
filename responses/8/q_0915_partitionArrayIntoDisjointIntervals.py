from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = partition_idx = curr_max = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < left_max:
                left_max = curr_max
                partition_idx = i
            else:
                curr_max = max(curr_max, nums[i])
        
        return partition_idx + 1
