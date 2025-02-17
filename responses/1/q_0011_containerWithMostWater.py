from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            curr_height = min(height[left], height[right])
            curr_width = right - left
            max_area = max(max_area, curr_height * curr_width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
