from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        max_reachable = 0
        n = len(nums)

        for i in range(n):
            if i > max_reachable:
                return False
            if i + nums[i] > max_reachable:
                max_reachable = i + nums[i]
            if max_reachable >= n - 1:
                return True

        return False
