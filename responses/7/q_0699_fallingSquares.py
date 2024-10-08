from typing import List

class Solution:
    
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ans = []
        intervals = [(0, 0, 0)]  # (start, end, height)
        max_height = 0
        
        for left, length in positions:
            right = left + length
            fall_height = 0
            
            for start, end, h in intervals:
                if left < end and right > start:  # If there's overlap
                    fall_height = max(fall_height, h)
            
            new_height = fall_height + length
            intervals.append((left, right, new_height))
            
            for i in range(len(intervals) - 1, -1, -1):
                il, ir, ih = intervals[i]
                if il < right and ir > left:
                    if new_height > ih:
                        intervals[i] = (il, ir, new_height)
                    max_height = max(max_height, new_height)
                        
        return ans
