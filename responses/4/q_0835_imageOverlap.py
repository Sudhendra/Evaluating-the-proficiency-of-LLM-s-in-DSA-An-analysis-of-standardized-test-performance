class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        max_count = 0

        def count_overlaps(shift_x, shift_y):
            count = 0
            for x1 in range(max(0, shift_x), min(n, n + shift_x)):
                for y1 in range(max(0, shift_y), min(n, n + shift_y)):
                    x2, y2 = x1 - shift_x, y1 - shift_y
                    if 0 <= x2 < n and 0 <= y2 < n and img1[x1][y1] == 1 and img2[x2][y2] == 1:
                        count += 1
            return count

        for shift_x in range(-n + 1, n):
            for shift_y in range(-n + 1, n):
                max_count = max(max_count, count_overlaps(shift_x, shift_y))

        return max_count
