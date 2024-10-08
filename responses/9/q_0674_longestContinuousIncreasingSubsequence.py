from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest_streak = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_streak += 1
                longest_streak = max(longest_streak, current_streak)
            else:
                current_streak = 1
                
        return longest_streak
