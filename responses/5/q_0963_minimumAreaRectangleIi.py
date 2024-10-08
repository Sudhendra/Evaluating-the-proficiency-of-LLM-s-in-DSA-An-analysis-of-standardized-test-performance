from typing import List

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        coordinates = set((x, y) for x, y in points)
        n = len(points)
        min_area = float('inf')
        
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                for k in range(j+1, n):
                    x3, y3 = points[k]
                    
                    if (x3-x1)*(x2-x1) + (y3-y1)*(y2-y1) == 0:
                        x4, y4 = x2+x3-x1, y2+y3-y1
                        if (x4, y4) in coordinates:
                            area = ((x2-x1)**2 + (y2-y1)**2) * ((x3-x1)**2 + (y3-y1)**2)
                            min_area = min(min_area, area)
        
        return 0 if min_area == float('inf') else min_area ** 0.5
