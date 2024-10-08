from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        def count_overlap(img1, img2):
            overlaps = defaultdict(int)
            n = len(img1)
            for i in range(n):
                for j in range(n):
                    if img1[i][j] == 1:
                        for x in range(n):
                            for y in range(n):
                                if img2[x][y] == 1:
                                    overlaps[(x-i, y-j)] += 1
            return max(overlaps.values()) if overlaps else 0
        
        return max(count_overlap(img1, img2), count_overlap(img2, img1))
