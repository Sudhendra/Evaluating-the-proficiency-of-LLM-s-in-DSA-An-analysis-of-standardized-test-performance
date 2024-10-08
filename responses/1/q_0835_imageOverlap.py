from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        count = defaultdict(int)
        result = 0

        img1_coords = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        img2_coords = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        for r1, c1 in img1_coords:
            for r2, c2 in img2_coords:
                count[(r1-r2, c1-c2)] += 1

        result = max(count.values()) if count else 0
        return result
