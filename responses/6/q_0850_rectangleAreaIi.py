from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]) -> int:
        MOD = 10**9 + 7

        x_set = set()
        y_set = set()

        for x1, y1, x2, y2 in rectangles:
            x_set.add(x1)
            x_set.add(x2)
            y_set.add(y1)
            y_set.add(y2)

        x_list = sorted(list(x_set))
        y_list = sorted(list(y_set))

        res = 0
        for i in range(len(x_list) - 1):
            for j in range(len(y_list) - 1):
                for x1, y1, x2, y2 in rectangles:
                    if x1 <= x_list[i] < x2 and y1 <= y_list[j] < y2:
                        res += (x_list[i+1] - x_list[i]) * (y_list[j+1] - y_list[j])
                        break

        return res % MOD
