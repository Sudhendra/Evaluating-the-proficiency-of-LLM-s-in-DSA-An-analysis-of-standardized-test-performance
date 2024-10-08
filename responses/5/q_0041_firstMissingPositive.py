from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Replace negative numbers, zeros, and numbers larger than n with a value greater than n
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Step 2: Mark the presence of each number in the array by changing the sign of the number at index (num - 1)
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # Step 3: Find the first positive number, its index + 1 is the answer
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # Step 4: If no positive number is found, the answer is n + 1
        return n + 1
