class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        def build_convex_hull(points):
            points.sort()
            hull = []
            for point in points:
                while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) < 0:
                    hull.pop()
                hull.append(point)
            for point in reversed(points[:-1]):
                while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) < 0:
                    hull.pop()
                hull.append(point)
            return hull

        return build_convex_hull(trees)