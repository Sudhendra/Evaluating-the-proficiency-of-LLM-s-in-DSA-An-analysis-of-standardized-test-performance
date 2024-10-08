from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def max_points_on_line(p1: List[int], p2: List[int]) -> int:
            if p1[0] == p2[0]:  # If both points are in the same x-axis
                slope = float('inf')
                intercept = p1[0]
            else:
                slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                intercept = p1[1] - slope * p1[0]

            return slope, intercept

        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        if len(points) < 3:
            return len(points)

        max_points = 0

        for i in range(len(points)):
            slopes_count = defaultdict(int)
            same_points = 0
            local_max = 0

            for j in range(i+1, len(points)):
                if points[i] == points[j]:
                    same_points += 1
                    continue

                slope, intercept = max_points_on_line(points[i], points[j])

                if slope == float('inf'):
                    slopes_count[(slope, intercept)] += 1
                    local_max = max(local_max, slopes_count[(slope, intercept)])
                else:
                    gcd_val = gcd(abs(points[j][1] - points[i][1]), abs(points[j][0] - points[i][0]))
                    key = (int((points[j][1] - points[i][1]) / gcd_val), int((points[j][0] - points[i][0]) / gcd_val), intercept)
                    slopes_count[key] += 1
                    local_max = max(local_max, slopes_count[key])

            max_points = max(max_points, local_max + same_points + 1)

        return max_points
