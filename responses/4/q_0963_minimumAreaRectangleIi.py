from itertools import combinations
from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]) -> float:
        points_set = {tuple(point) for point in points}
        seen_rectangles = defaultdict(list)
        min_area = float('inf')

        for p1, p2, p3 in combinations(points, 3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3

            # Check if p1, p2, p3 could form a diagonal of a potential rectangle
            if (x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1) == 0:
                center_x = (x1 + x2) / 2
                center_y = (y1 + y2) / 2
                rectangle_diagonal = (x2 - x1) ** 2 + (y2 - y1) ** 2
                seen_rectangles[(center_x, center_y, rectangle_diagonal)].append(p1)

        for (center_x, center_y, rectangle_diagonal), candidates in seen_rectangles.items():
            for p1, p2 in combinations(candidates, 2):
                x1, y1 = p1
                x2, y2 = p2
                x4 = 2 * center_x - x1
                y4 = 2 * center_y - y1

                if (x4, y4) in points_set:
                    min_area = min(min_area, rectangle_diagonal)

        return 0 if min_area == float('inf') else min_area ** 0.5
