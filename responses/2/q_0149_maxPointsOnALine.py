class Solution:
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)

        max_points = 2
        for i in range(len(points)):
            slopes = {}
            same_points = 1

            for j in range(len(points)):
                if i == j:
                    continue

                if points[i] == points[j]:
                    same_points += 1
                    continue

                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0:
                    slope = (float('inf'), float('inf'))
                else:
                    slope = dy / dx

                slopes[slope] = slopes.get(slope, 1) + 1

            max_points = max(max_points, max(slopes.values()) + same_points)

        return max_points