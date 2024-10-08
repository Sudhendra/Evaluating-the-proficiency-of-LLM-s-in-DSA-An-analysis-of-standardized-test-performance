from typing import List

class Solution:

    def isRectangleCover(self, rectangles: List[List[int]) -> bool:
        if not rectangles:
            return False

        left = min(rectangles, key=lambda x: x[0])[0]
        bottom = min(rectangles, key=lambda x: x[1])[1]
        right = max(rectangles, key=lambda x: x[2])[2]
        top = max(rectangles, key=lambda x: x[3])[3]

        total_area = 0
        points = set()
        
        for x1, y1, x2, y2 in rectangles:
            total_area += (x2 - x1) * (y2 - y1)
            for point in [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]:
                if point in points:
                    points.discard(point)
                else:
                    points.add(point)

        if total_area != ((right - left) * (top - bottom)):
            return False

        if (left, bottom) not in points or (right, bottom) not in points or (left, top) not in points or (right, top) not in points:
            return False

        return len(points) == 4
