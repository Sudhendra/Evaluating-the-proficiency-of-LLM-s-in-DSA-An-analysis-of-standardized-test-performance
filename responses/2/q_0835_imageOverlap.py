from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        offsets = defaultdict(int)
        max_overlap = 0

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    for x in range(n):
                        for y in range(n):
                            if img2[x][y] == 1:
                                offset = (x - i, y - j)
                                offsets[offset] += 1
                                max_overlap = max(max_overlap, offsets[offset])

        return max_overlap
