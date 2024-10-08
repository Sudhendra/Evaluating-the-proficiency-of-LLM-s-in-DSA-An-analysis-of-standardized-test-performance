from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]) -> bool:
        def area(x1, y1, x2, y2):
            return (x2 - x1) * (y2 - y1)

        corners = set()
        total_area = 0

        for x1, y1, x2, y2 in rectangles:
            total_area += area(x1, y1, x2, y2)
            corners ^= {(x1, y1), (x2, y2), (x1, y2), (x2, y1)}

        if len(corners) != 4:
            return False

        corners = sorted(corners)
        x1, y1 = corners[0]
        x2, y2 = corners[-1]

        return total_area == area(x1, y1, x2, y2)
