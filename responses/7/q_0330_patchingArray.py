from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        covered = 0
        index = 0

        while covered < n:
            if index < len(nums) and nums[index] <= covered + 1:
                covered += nums[index]
                index += 1
            else:
                covered += covered + 1
                patches += 1

        return patches

# Example usage:
sol = Solution()
print(sol.minPatches([1, 3], 6))  # Output should be 1
print(sol.minPatches([1, 5, 10], 20))  # Output should be 2
print(sol.minPatches([1, 2, 2], 5))  # Output should be 0
