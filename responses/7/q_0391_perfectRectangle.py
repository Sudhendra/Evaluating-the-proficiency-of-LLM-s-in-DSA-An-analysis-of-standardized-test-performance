from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]) -> bool:
        # Initialize variables to keep track of boundaries for the large rectangle
        boundaries = set()
        x1, y1, x2, y2 = float('inf'), float('inf'), float('-inf'), float('-inf')
        
        # Initialize variable to keep track of total area of all small rectangles
        total_area = 0
        
        for x1_cur, y1_cur, x2_cur, y2_cur in rectangles:
            x1 = min(x1, x1_cur)
            y1 = min(y1, y1_cur)
            x2 = max(x2, x2_cur)
            y2 = max(y2, y2_cur)
            
            total_area += (x2_cur - x1_cur) * (y2_cur - y1_cur)
            
            for point in [(x1_cur, y1_cur), (x1_cur, y2_cur), (x2_cur, y1_cur), (x2_cur, y2_cur)]:
                if point in boundaries:
                    boundaries.remove(point)
                else:
                    boundaries.add(point)
        
        if (x1, y1, x2, y2) != (x1_cur, y1_cur, x2_cur, y2_cur):
            return False
        
        for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
            if point not in boundaries:
                return False
        
        if total_area != (x2 - x1) * (y2 - y1):
            return False
        
        return True
