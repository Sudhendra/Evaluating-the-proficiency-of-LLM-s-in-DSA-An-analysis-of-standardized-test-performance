from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        total = 0
        for p in points:
            distances = {}
            for q in points:
                if p == q:
                    continue
                d = distance(p, q)
                distances[d] = distances.get(d, 0) + 1
                
            for d in distances:
                total += distances[d] * (distances[d] - 1)

        return total
