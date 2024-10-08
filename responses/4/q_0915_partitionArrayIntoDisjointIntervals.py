from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = nums[0]
        max_global = max_left
        partition_idx = 0

        for i in range(1, n):
            if nums[i] < max_left:
                max_left = max_global
                partition_idx = i
            else:
                max_global = max(max_global, nums[i])

        return partition_idx + 1
