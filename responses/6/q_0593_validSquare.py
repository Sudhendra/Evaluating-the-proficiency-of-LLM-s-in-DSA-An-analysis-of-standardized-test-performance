from typing import List

class Solution:

    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        def dist(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

        def is_square(p1, p2, p3, p4):
            dists = []
            dists.append(dist(p1, p2))
            dists.append(dist(p1, p3))
            dists.append(dist(p1, p4))
            dists.append(dist(p2, p3))
            dists.append(dist(p2, p4))
            dists.append(dist(p3, p4))
            
            dists.sort()
            
            return dists[0] != 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5]

        return is_square(p1, p2, p3, p4) or is_square(p1, p3, p2, p4) or is_square(p1, p4, p2, p3)

