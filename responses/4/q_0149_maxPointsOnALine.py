from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def max_points_on_line(p1, p2):
            if p1[0] == p2[0]:
                return (float('inf'), p1[0])
            elif p1[1] == p2[1]:
                return (0, p1[1])
            else:
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                d = gcd(dx, dy)
                return (dy // d, dx // d, p1[1]*dx - p1[0]*dy)

        if len(points) < 3:
            return len(points)

        max_points = 0
        for i in range(len(points)):
            gradients = defaultdict(int)
            same_points = 0
            local_max = 0
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    same_points += 1
                else:
                    slope = max_points_on_line(points[i], points[j])
                    gradients[slope] += 1
                    local_max = max(local_max, gradients[slope])

            max_points = max(max_points, local_max + same_points + 1)

        return max_points
