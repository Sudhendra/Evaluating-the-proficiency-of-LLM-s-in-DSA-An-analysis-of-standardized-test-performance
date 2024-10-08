from typing import List

class Solution:
    def orientation(self, p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def build_convex_hull(self, points):
        points.sort(key=lambda x: (x[0], x[1]))
        upper_hull = []
        lower_hull = []
        
        for p in points:
            while len(upper_hull) >= 2 and self.orientation(upper_hull[-2], upper_hull[-1], p) > 0:
                upper_hull.pop()
            upper_hull.append(p)
            
        for p in reversed(points):
            while len(lower_hull) >= 2 and self.orientation(lower_hull[-2], lower_hull[-1], p) > 0:
                lower_hull.pop()
            lower_hull.append(p)
        
        return upper_hull[:-1] + lower_hull[:-1]

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 1:
            return trees
        
        if len(trees) == 2:
            return trees

        convex_hull = self.build_convex_hull(trees)
        
        return convex_hull
