from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        def on_segment(p, q, r):
            return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])

        def convex_hull(points):
            points.sort()
            hull = []
            for point in points:
                while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) > 0:
                    hull.pop()
                hull.append(point)
            for i in range(len(points) - 2, -1, -1):
                while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) > 0:
                    hull.pop()
                hull.append(points[i])
            return list(set(tuple(x) for x in hull))
        
        return convex_hull(trees)
