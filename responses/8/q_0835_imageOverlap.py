from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        img1_points = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        img2_points = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
        
        offsets = defaultdict(int)
        result = 0
        
        for x1, y1 in img1_points:
            for x2, y2 in img2_points:
                offset = (x1 - x2, y1 - y2)
                offsets[offset] += 1
                result = max(result, offsets[offset])
        
        return result
