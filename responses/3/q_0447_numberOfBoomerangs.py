from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

        total = 0
        for p1 in points:
            distances = {}
            for p2 in points:
                d = distance(p1, p2)
                distances[d] = distances.get(d, 0) + 1

            for count in distances.values():
                total += count * (count - 1)  # n * (n-1) permutations for each distance

        return total
