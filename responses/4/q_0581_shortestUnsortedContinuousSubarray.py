from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        start, end = -1, -2
        min_val, max_val = float('inf'), float('-inf')
        
        for i in range(n):
            max_val = max(max_val, nums[i])
            min_val = min(min_val, nums[n - 1 - i])
            if nums[i] < max_val:
                end = i
            if nums[n - 1 - i] > min_val:
                start = n - 1 - i
        
        return end - start + 1
