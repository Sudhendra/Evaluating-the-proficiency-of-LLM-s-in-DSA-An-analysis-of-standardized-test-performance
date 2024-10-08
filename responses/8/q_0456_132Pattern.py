from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        min_left = [nums[0]]
        for i in range(1, n):
            min_left.append(min(min_left[-1], nums[i]))
        
        stack = []
        for j in range(n-1, 0, -1):
            if nums[j] > min_left[j-1]:
                while stack and stack[-1] <= min_left[j-1]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        
        return False
