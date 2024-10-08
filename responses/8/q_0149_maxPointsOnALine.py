from collections import defaultdict
from fractions import Fraction

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        def slope(p1, p2):
            if p1[0] == p2[0]:
                return float('inf')
            return Fraction(p1[1] - p2[1], p1[0] - p2[0])

        def max_points_on_line(start):
            max_count = 0
            same_points = 0
            slopes = defaultdict(int)

            for i in range(start + 1, len(points)):
                if points[start] == points[i]:
                    same_points += 1
                    continue
                curr_slope = slope(points[start], points[i])
                slopes[curr_slope] += 1
                max_count = max(max_count, slopes[curr_slope])

            return max_count + same_points + 1

        max_points = 0
        for i in range(len(points) - 1):
            max_points = max(max_points, max_points_on_line(i))

        return max_points
