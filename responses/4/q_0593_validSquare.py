from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

        points = [p1, p2, p3, p4]
        distances = set()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distances.add(dist(points[i], points[j]))

        if len(distances) != 2:
            return False

        side, diagonal = sorted(distances)
        return side != 0 and side * 2 == diagonal
