from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ans = []
        heights = [(0, 0)]  # (start, end) position, and its height
        max_height = 0
        
        for left, side_length in positions:
            right = left + side_length
            start_height = 0
            for s, e, h in heights:
                if left < e and right > s:
                    start_height = max(start_height, h)
            
            new_height = start_height + side_length
            heights.append((left, right, new_height))
            max_height = max(max_height, new_height)
            ans.append(max_height)
        
        return ans
