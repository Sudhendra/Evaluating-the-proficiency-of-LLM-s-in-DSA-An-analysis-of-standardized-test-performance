from typing import List

class Solution:
    def orientation(self, p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort(key=lambda x: (x[0], x[1]))
        
        def build_hull(points):
            hull = []
            for point in points:
                while len(hull) >= 2 and self.orientation(hull[-2], hull[-1], point) < 0:
                    hull.pop()
                hull.append(point)
                
            return hull
        
        lower_hull = build_hull(trees)
        upper_hull = build_hull(trees[::-1])
        full_hull = lower_hull + upper_hull
        
        return [list(point) for point in set(map(tuple, full_hull))]