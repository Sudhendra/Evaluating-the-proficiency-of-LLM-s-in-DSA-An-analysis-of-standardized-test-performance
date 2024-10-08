from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        min_vals = [0] * n
        min_vals[0] = nums[0]
        
        for i in range(1, n):
            min_vals[i] = min(min_vals[i - 1], nums[i])
        
        stack = []
        
        for j in range(n - 1, -1, -1):
            if nums[j] > min_vals[j]:
                while stack and stack[-1] <= min_vals[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        
        return False
