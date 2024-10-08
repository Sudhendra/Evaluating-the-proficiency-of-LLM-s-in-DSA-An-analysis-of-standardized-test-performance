from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]) -> bool:
        points = set()
        area = 0

        for rect in rectangles:
            x1, y1, x2, y2 = rect
            area += (x2 - x1) * (y2 - y1)

            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)

        if len(points) != 4:
            return False

        x1, y1 = min(points)
        x2, y2 = max(points)

        return area == (x2 - x1) * (y2 - y1)
