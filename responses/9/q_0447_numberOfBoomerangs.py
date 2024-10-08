from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def get_distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        count = 0
        for p in points:
            distances = defaultdict(int)
            for q in points:
                distances[get_distance(p, q)] += 1
            for distance in distances.values():
                count += distance * (distance - 1)

        return count
