from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        shifts = defaultdict(int)
        ones1, ones2 = [], []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))
                if img2[i][j] == 1:
                    ones2.append((i, j))

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                shifts[(x2-x1, y2-y1)] += 1

        return max(shifts.values(), default=0)
