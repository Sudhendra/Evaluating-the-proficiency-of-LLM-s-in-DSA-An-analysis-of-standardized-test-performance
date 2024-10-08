from typing import List

class Solution:
    def distance(self, p1: List[int], p2: List[int]) -> int:
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for p in points:
            distances = {}
            for q in points:
                d = self.distance(p, q)
                distances[d] = distances.get(d, 0) + 1
            for key in distances:
                total += distances[key] * (distances[key] - 1)
        return total
