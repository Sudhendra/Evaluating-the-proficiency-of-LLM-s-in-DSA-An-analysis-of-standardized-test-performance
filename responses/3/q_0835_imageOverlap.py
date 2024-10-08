from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        A = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        B = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
        counter = defaultdict(int)
        for a in A:
            for b in B:
                offset = (a[0] - b[0], a[1] - b[1])
                counter[offset] += 1
        return max(counter.values() or [0])
