from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def calculate_area(p1, p2, p3):
            return 0.5 * abs(p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[1]*p2[0] - p2[1]*p3[0] - p3[1]*p1[0])

        max_area = 0
        for p1, p2, p3 in combinations(points, 3):
            area = calculate_area(p1, p2, p3)
            max_area = max(max_area, area)

        return max_area