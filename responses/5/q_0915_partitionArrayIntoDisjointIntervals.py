from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        maxLeft = [0] * n
        minRight = [0] * n

        maxLeft[0] = nums[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], nums[i])

        minRight[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            minRight[i] = min(minRight[i + 1], nums[i])

        for i in range(1, n):
            if maxLeft[i - 1] <= minRight[i]:
                return i

        return -1
