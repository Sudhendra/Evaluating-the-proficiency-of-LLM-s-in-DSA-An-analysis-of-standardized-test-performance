from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]) -> bool:
        if not rectangles:
            return False

        corners = set()
        total_area = 0

        for rect in rectangles:
            x1, y1, x2, y2 = rect
            total_area += (x2 - x1) * (y2 - y1)

            corners ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}

        if len(corners) != 4:
            return False

        corners = sorted(corners)
        x1, y1 = corners[0]
        x2, y2 = corners[-1]

        return total_area == (x2 - x1) * (y2 - y1)
