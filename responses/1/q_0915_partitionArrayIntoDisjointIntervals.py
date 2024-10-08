from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = nums[0]  # max element in left part
        max_so_far = nums[0]  # max element so far

        partition_idx = 0

        for i in range(1, len(nums)):
            if nums[i] < left_max:  # need to move partition to right
                partition_idx = i
                left_max = max_so_far
            else:
                max_so_far = max(max_so_far, nums[i])

        return partition_idx + 1