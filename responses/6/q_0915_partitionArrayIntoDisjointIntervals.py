class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = left_max = nums[0]
        partition_idx = 0

        for i in range(1, n):
            if nums[i] < max_left:
                max_left = left_max  # Update left_max to the maximum value seen so far
                partition_idx = i
            else:
                left_max = max(left_max, nums[i])  # Update left_max for next iteration

        return partition_idx + 1
