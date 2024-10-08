from itertools import combinations

class Solution:
    def minAreaFreeRect(self, points):
        point_set = {complex(*point) for point in points}
        min_area = float('inf')

        for p1, p2, p3 in combinations(points, 3):
            v1 = complex(p1[0], p1[1])
            v2 = complex(p2[0], p2[1])
            v3 = complex(p3[0], p3[1])

            v12 = v2 - v1
            v13 = v3 - v1

            if v12 and v13 and v12.real * v13.real + v12.imag * v13.imag == 0:
                v4 = v1 + v12 + v13
                if v4 in point_set:
                    area = abs(v12) * abs(v13)
                    min_area = min(min_area, area)

        return min_area if min_area != float('inf') else 0
