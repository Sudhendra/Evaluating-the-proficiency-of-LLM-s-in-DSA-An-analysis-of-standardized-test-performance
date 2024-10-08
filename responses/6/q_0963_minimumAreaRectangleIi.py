from itertools import combinations

class Solution:
    def minAreaFreeRect(self, points: List[List[int]) -> float:
        points_set = set(map(tuple, points))
        min_area = float('inf')

        for p1, p2, p3 in combinations(points, 3):
            p4 = (p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1])
            
            if p4 in points_set:
                area = ((p2[0] - p1[0]) * (p3[0] - p1[0]) + (p2[1] - p1[1]) * (p3[1] - p1[1]))
                min_area = min(min_area, area)

        return min_area if min_area < float('inf') else 0.0
