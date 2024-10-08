class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. Set negative numbers and numbers greater than n to 0
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 0
        
        # 2. Mark the presence of numbers by setting corresponding index element to negative
        for i in range(n):
            idx = abs(nums[i]) - 1
            if idx < n and nums[idx] > 0:
                nums[idx] = -nums[idx]
        
        # 3. Find the first missing positive integer
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        
        return n + 1
