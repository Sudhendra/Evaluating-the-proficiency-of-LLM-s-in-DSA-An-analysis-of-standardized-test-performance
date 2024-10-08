from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]) -> int:
        def distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        count = 0

        for point in points:
            dist_map = defaultdict(int)

            for other_point in points:
                if point == other_point:
                    continue

                dist = distance(point, other_point)
                dist_map[dist] += 1

            for key in dist_map:
                count += dist_map[key] * (dist_map[key] - 1)

        return count
