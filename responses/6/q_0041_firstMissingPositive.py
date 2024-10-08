from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Replace negative numbers and numbers greater than n with 0
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 0

        # Mark presence of numbers (1 to n) using the array itself as a hashmap
        for i in range(n):
            if 1 <= abs(nums[i]) <= n:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])

        # Find the first missing positive integer
        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        return n + 1
