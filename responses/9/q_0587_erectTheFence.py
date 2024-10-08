from typing import List

class Solution:
    def orientation(self, p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def convex_hull(self, points):
        n = len(points)
        if n <= 1:
            return points
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
        return lower[:-1] + upper[:-1]

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort()
        return self.convex_hull(trees)
