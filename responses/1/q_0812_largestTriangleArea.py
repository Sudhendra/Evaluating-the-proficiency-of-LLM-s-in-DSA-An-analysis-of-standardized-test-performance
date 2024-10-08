from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a, b, c):
            return 0.5 * abs(a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - a[1]*b[0] - b[1]*c[0] - c[1]*a[0])
        
        max_area = 0
        for comb in combinations(points, 3):
            max_area = max(max_area, area(*comb))
        
        return max_area
