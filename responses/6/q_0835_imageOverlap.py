from collections import Counter

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        img1_points = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        img2_points = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        overlap_counter = Counter((p1[0] - p2[0], p1[1] - p2[1]) for p1 in img1_points for p2 in img2_points)
        return max(overlap_counter.values(), default=0)
