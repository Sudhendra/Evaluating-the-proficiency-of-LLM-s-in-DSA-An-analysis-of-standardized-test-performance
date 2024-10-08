from typing import List
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n
        
        max_points = 1
        for i in range(n):
            slope_count = defaultdict(int)
            same_points = 0
            local_max = 1
            for j in range(i+1, n):
                if points[i] == points[j]:
                    same_points += 1
                else:
                    dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                    # Reduce to simplest form
                    gcd_val = math.gcd(dx, dy)
                    slope = (dx // gcd_val, dy // gcd_val)
                    slope_count[slope] += 1
                    local_max = max(local_max, slope_count[slope] + 1)
            
            max_points = max(max_points, local_max + same_points)
        
        return max_points