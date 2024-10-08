class Solution:
    def maxPoints(self, points: List[List[int]) -> int:
        from collections import defaultdict
        if len(points) < 3:
            return len(points)

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        def slope(p1, p2):
            dx, dy = p1[0] - p2[0], p1[1] - p2[1]
            if dx == 0:
                return (0, 1)
            if dy == 0:
                return (1, 0)
            g = gcd(dx, dy)
            return (dx // g, dy // g)

        def max_points_on_line_containing_point_i(i):
            same_point = 0
            slopes = defaultdict(int)
            max_points = 1

            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    same_point += 1
                    continue

                cur_slope = slope(points[i], points[j])
                slopes[cur_slope] += 1
                max_points = max(max_points, slopes[cur_slope])

            return max_points + same_point + 1

        max_points = 1
        for i in range(len(points) - 1):
            max_points = max(max_points, max_points_on_line_containing_point_i(i))

        return max_points