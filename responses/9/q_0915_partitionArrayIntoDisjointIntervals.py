from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = nums[0]
        overall_max = max_left
        partition_idx = 0
        
        for i in range(1, n):
            if nums[i] < max_left:
                partition_idx = i
                max_left = overall_max
            else:
                overall_max = max(overall_max, nums[i])
        
        return partition_idx + 1
