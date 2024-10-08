from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        mins = [0] * n
        mins[0] = nums[0]
        for i in range(1, n):
            mins[i] = min(mins[i - 1], nums[i])
        
        stack = []
        for j in range(n - 1, 0, -1):
            if nums[j] > mins[j]:
                while stack and stack[-1] <= mins[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        
        return False
