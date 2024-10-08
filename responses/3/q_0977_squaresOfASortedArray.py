from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        result = [0] * n
        current_pos = n - 1
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[current_pos] = nums[left] ** 2
                left += 1
            else:
                result[current_pos] = nums[right] ** 2
                right -= 1
            current_pos -= 1
        
        return result