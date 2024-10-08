from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]

        for point in points[1:]:
            if point[0] > end:
                arrows += 1
                end = point[1]

        return arrows
