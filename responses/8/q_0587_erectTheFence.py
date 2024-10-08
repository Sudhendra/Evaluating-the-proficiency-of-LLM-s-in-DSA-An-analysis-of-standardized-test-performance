from typing import List

class Solution:
    def orientation(self, p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def build_hull(points):
            points.sort()
            hull = []
            for p in points:
                while len(hull) >= 2 and self.orientation(hull[-2], hull[-1], p) < 0:
                    hull.pop()
                hull.append(p)
            hull.pop()
            for p in reversed(points):
                while len(hull) >= 2 and self.orientation(hull[-2], hull[-1], p) < 0:
                    hull.pop()
                hull.append(p)
            return hull
        
        points = sorted(trees)
        upper_hull = build_hull(points)
        
        points_set = set(map(tuple, points))
        result = [list(point) for point in points_set]
        
        return result

# Example usage
solution = Solution()
trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
print(solution.outerTrees(trees))
