from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(points)
        if n < 3:
            return n

        maxPoints = 0

        for i in range(n):
            slopes = defaultdict(int)
            samePoint = 1
            for j in range(i + 1, n):
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    samePoint += 1
                else:
                    g = gcd(dx, dy)
                    slope = (dy // g, dx // g)  # normalize to the smallest slope
                    slopes[slope] += 1

            if not slopes:
                maxPoints = max(maxPoints, samePoint)
            else:
                maxPoints = max(maxPoints, samePoint + max(slopes.values()))

        return maxPoints
