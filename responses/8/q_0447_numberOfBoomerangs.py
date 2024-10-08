from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]) -> int:
        result = 0
        for i in range(len(points)):
            point_map = {}
            for j in range(len(points)):
                if i == j:
                    continue
                distance = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                if distance in point_map:
                    point_map[distance] += 1
                else:
                    point_map[distance] = 1
            for key in point_map:
                result += point_map[key] * (point_map[key] - 1)
        return result
