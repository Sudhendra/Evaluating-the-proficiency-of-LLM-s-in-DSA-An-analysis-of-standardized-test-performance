from itertools import combinations

class Solution:
    def largestTriangleArea(self, points):
        def area(p, q, r):
            return 0.5 * abs(p[0]*q[1] + q[0]*r[1] + r[0]*p[1] - p[1]*q[0] - q[1]*r[0] - r[1]*p[0])
        
        max_area = 0
        for p, q, r in combinations(points, 3):
            max_area = max(max_area, area(p, q, r))
        
        return max_area
