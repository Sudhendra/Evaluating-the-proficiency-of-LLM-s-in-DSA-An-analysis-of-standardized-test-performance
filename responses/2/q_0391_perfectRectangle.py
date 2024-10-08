from typing import List

class Solution:
    
    def isRectangleCover(self, rectangles: List[List[int]) -> bool:
        points = set()
        area = 0
        
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            area += (x2 - x1) * (y2 - y1)
            p1 = (x1, y1)
            p2 = (x2, y2)
            p3 = (x1, y2)
            p4 = (x2, y1)
            
            for p in [p1, p2, p3, p4]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)
        
        if len(points) != 4:
            return False
        
        points = sorted(points)
        x1, y1 = points[0]
        x2, y2 = points[-1]
        
        expected_area = (x2 - x1) * (y2 - y1)
        
        return area == expected_area
