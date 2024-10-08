from typing import List

class Solution:
    def orientation(self, p, q, r):
        return (q[1] - p[1])*(r[0] - q[0]) - (q[0] - p[0])*(r[1] - q[1])

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def build_convex_hull(points):
            points.sort(key=lambda x: (x[0], x[1]))
            lower = []
            for p in points:
                while len(lower) >= 2 and self.orientation(lower[-2], lower[-1], p) < 0:
                    lower.pop()
                lower.append(p)

            upper = []
            for p in reversed(points):
                while len(upper) >= 2 and self.orientation(upper[-2], upper[-1], p) < 0:
                    upper.pop()
                upper.append(p)

            return list(set(tuple(i) for i in lower[:-1] + upper[:-1]))

        return build_convex_hull(trees)
