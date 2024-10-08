from typing import List

class Solution:
    def orientation(self, p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def on_boundary(self, p, q, r):
        return p[0] <= max(q[0], r[0]) and p[0] >= min(q[0], r[0]) and \
               p[1] <= max(q[1], r[1]) and p[1] >= min(q[1], r[1])

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 1:
            return trees

        def compare(a, b):
            return a[0] == b[0] and a[1] == b[1]

        trees.sort(key=lambda x: (x[0], x[1]))
        lower = []
        for tree in trees:
            while len(lower) >= 2 and self.orientation(lower[-2], lower[-1], tree) < 0:
                lower.pop()
            lower.append(tree)

        upper = []
        for tree in reversed(trees):
            while len(upper) >= 2 and self.orientation(upper[-2], upper[-1], tree) < 0:
                upper.pop()
            upper.append(tree)

        res = []
        for tree in lower:
            if tree not in res:
                res.append(tree)
        for tree in upper:
            if tree not in res and not compare(tree, lower[0]):
                res.append(tree)

        return res
