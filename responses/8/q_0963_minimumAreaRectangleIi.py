from itertools import combinations
from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points_set = {tuple(point) for point in points}
        n = len(points)
        distances = defaultdict(list)

        for P, Q in combinations(points, 2):
            center = ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
            distance = (P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2
            distances[(center, distance)].append(P)

        min_area = float('inf')
        for (center, distance), pair in distances.items():
            for P in pair:
                Q = (2 * center[0] - P[0], 2 * center[1] - P[1])
                if Q in points_set:
                    area = distance ** 0.5 * ((P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2) ** 0.5
                    min_area = min(min_area, area)

        return min_area if min_area != float('inf') else 0.0
