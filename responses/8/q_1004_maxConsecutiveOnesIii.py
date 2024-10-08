from typing import List

class Solution:
    """Given a binary array `nums` and an integer `k`, return *the maximum number of consecutive* `1`*'s in the array if you can flip at most* `k` `0`'s."""

    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        max_ones = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
                
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            max_ones = max(max_ones, right - left + 1)
        
        return max_ones

# Example usage
sol = Solution()
print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # Output: 6
print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # Output: 10
