from typing import List

class Solution:
    def distance(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
    
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points_set = set((x, y) for x, y in points)
        result = float('inf')
        
        for p1, p2, p3 in itertools.combinations(points, 3):
            p4 = (p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1])
            if p4 in points_set:
                d1 = self.distance(p1, p2)
                d2 = self.distance(p1, p3)
                result = min(result, d1 * d2)
        
        return result if result != float('inf') else 0.0
