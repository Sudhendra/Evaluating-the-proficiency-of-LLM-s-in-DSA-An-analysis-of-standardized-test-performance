from collections import defaultdict
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def get_slope(p1, p2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx == 0:
                return (0, 1)
            elif dy == 0:
                return (1, 0)
            else:
                d = gcd(dx, dy)
                return (dx // d, dy // d)

        max_points = 0
        for i in range(n):
            slopes = defaultdict(int)
            same_point = 1
            local_max = 0
            for j in range(n):
                if i != j:
                    if points[i] == points[j]:
                        same_point += 1
                    else:
                        slope = get_slope(points[i], points[j])
                        slopes[slope] += 1
                        local_max = max(local_max, slopes[slope])

            max_points = max(max_points, local_max + same_point)

        return max_points
