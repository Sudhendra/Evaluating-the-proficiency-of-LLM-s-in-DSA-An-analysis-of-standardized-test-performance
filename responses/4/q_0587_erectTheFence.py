from typing import List

class Solution:
    def orientation(self, p, q, r) -> int:
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def onSegment(self, p, q, r) -> bool:
        return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 1:
            return trees

        def getHull(trees):
            trees.sort(key=lambda x: (x[0], x[1]))

            upper = []
            for tree in trees:
                while len(upper) >= 2 and self.orientation(upper[-2], upper[-1], tree) > 0:
                    upper.pop()
                upper.append(tree)

            lower = []
            for tree in reversed(trees):
                while len(lower) >= 2 and self.orientation(lower[-2], lower[-1], tree) > 0:
                    lower.pop()
                lower.append(tree)

            return list(set(map(tuple, upper[:-1] + lower[:-1])))

        return getHull(trees)
