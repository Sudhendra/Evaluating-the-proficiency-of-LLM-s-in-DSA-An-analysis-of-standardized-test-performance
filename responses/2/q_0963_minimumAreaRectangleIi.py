from itertools import combinations
from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points_set = set((x, y) for x, y in points)
        area = float('inf')

        for p1, p2, p3 in combinations(points, 3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3

            if (x4 := x2 + x3 - x1, y4 := y2 + y3 - y1) in points_set:
                area = min(area, ((x2-x1)*(x3-x1) + (y2-y1)*(y3-y1)))

        return area if area != float('inf') else 0.0
