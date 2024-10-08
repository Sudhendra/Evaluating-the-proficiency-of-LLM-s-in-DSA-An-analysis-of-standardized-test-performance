from typing import List

class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)
        
        def count_boomerangs(p1, points):
            distances = {}
            for p2 in points:
                d = distance(p1, p2)
                distances[d] = distances.get(d, 0) + 1
                
            count = 0
            for d in distances.values():
                count += d * (d - 1)  # Permutations of 2 elements from d
            return count

        total_boomerangs = 0
        for p1 in points:
            total_boomerangs += count_boomerangs(p1, [p for p in points if p != p1])
        
        return total_boomerangs
