from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Do not return anything, modify nums in-place instead.
        
        # Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Find the smallest element larger than nums[i] from the right
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the sub-array from i+1 to the end
        nums[i+1:] = nums[i+1:][::-1]
