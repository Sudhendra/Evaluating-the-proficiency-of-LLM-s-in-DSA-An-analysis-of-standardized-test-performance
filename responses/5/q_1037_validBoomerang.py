from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        
        # Check if the points are distinct and not in a straight line
        return (x1 - x2) * (y1 - y3) != (x1 - x3) * (y1 - y2)
