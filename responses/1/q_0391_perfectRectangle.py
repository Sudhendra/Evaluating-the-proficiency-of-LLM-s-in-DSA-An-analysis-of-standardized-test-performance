class Solution:
    def isRectangleCover(self, rectangles: List[List[int]) -> bool:
        points = set()
        area = 0
        
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            area += (x2 - x1) * (y2 - y1)
            
            p1 = (x1, y1)
            p2 = (x1, y2)
            p3 = (x2, y1)
            p4 = (x2, y2)
            
            for p in [p1, p2, p3, p4]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)
        
        if len(points) != 4:
            return False
        
        x1, y1 = min(points)
        x2, y2 = max(points)
        
        return area == (x2 - x1) * (y2 - y1)