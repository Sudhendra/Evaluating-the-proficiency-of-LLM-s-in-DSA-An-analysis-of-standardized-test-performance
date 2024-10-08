from itertools import combinations
from collections import defaultdict
import math

class Solution:
    def minAreaFreeRect(self, points: List[List[int]) -> float:
        point_set = {tuple(point) for point in points}
        diagonal_pairs = defaultdict(list)
        min_area = float('inf')
        
        for p1, p2, p3 in combinations(points, 3):
            diagonal_vector = (p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1])
            fourth_point = (p2[0] - p3[0] + p1[0], p2[1] - p3[1] + p1[1])
            if fourth_point in point_set:
                area = math.hypot(diagonal_vector[0], diagonal_vector[1]) * math.hypot(p2[0] - p1[0], p2[1] - p1[1])
                min_area = min(min_area, area)
        
        return min_area if min_area != float('inf') else 0.0
