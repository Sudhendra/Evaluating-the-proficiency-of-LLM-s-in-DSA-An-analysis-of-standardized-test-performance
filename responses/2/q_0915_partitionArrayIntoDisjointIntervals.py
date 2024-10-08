from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = [0] * n
        min_right = [0] * n

        max_val = float('-inf')
        for i in range(n):
            max_val = max(max_val, nums[i])
            max_left[i] = max_val

        min_val = float('inf')
        for i in range(n-1, -1, -1):
            min_val = min(min_val, nums[i])
            min_right[i] = min_val

        for i in range(1, n):
            if max_left[i-1] <= min_right[i]:
                return i
