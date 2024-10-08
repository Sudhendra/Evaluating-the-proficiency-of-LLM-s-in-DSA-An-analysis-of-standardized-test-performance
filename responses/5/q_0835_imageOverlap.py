from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        img1_points = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        img2_points = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        
        offsets = Counter((x1 - x2, y1 - y2) for x1, y1 in img1_points for x2, y2 in img2_points)

        return max(offsets.values()) if offsets else 0
