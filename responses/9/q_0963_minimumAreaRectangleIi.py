from typing import List
from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        point_set = {tuple(point) for point in points}
        n = len(points)
        area = float('inf')
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    if (x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1) == 0:
                        x4, y4 = x3 + x2 - x1, y3 + y2 - y1
                        if (x4, y4) in point_set:
                            area = min(area, ((x2 - x1)**2 + (y2 - y1)**2) * ((x3 - x1)**2 + (y3 - y1)**2))
        return 0 if area == float('inf') else area**0.5
