from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]) -> bool:
        points = set()
        total_area = 0
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            total_area += (x2 - x1) * (y2 - y1)
            for point in [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]:
                if point in points:
                    points.remove(point)
                else:
                    points.add(point)

        if len(points) != 4 or total_area != (max(p[0] for p in points) - min(p[0] for p in points)) * (max(p[1] for p in points) - min(p[1] for p in points)):
            return False

        corner_points = {(min(p[0] for p in points), min(p[1] for p in points)),
                         (min(p[0] for p in points), max(p[1] for p in points)),
                         (max(p[0] for p in points), min(p[1] for p in points)),
                         (max(p[0] for p in points), max(p[1] for p in points))}

        return points == corner_points
