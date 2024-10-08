from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            min_height = min(height[left], height[right])
            width = right - left
            max_area = max(max_area, min_height * width)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
